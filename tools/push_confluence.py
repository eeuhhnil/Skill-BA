"""Đẩy một file Markdown lên Confluence Data Center thành trang con.

Tạo trang mới dưới trang cha; nếu trong space đã có trang cùng tiêu đề thì cập nhật (tăng version).

Token: Personal Access Token của Confluence, đọc từ biến môi trường CONFLUENCE_PAT
hoặc từ file %USERPROFILE%\\.confluence-pat (một dòng, chỉ chứa token).

Ví dụ:
  python tools/push_confluence.py docs/briefs/.../brief.md --dry-run
  python tools/push_confluence.py docs/briefs/.../brief.md
  python tools/push_confluence.py docs/briefs/.../addendum.md --parent-title "Kiểm kê kho — Giải pháp sơ bộ"
"""
import argparse
import os
import re
import sys
from pathlib import Path

import markdown
import requests

BASE_URL = "https://confluence-sds.softdreams.vn:8090"
SPACE_KEY = "EP"
PARENT_ID = "50697857"  # Tài liệu nghiệp vụ


def load_token():
    token = os.environ.get("CONFLUENCE_PAT")
    if not token:
        token_file = Path.home() / ".confluence-pat"
        if token_file.exists():
            token = token_file.read_text(encoding="utf-8").strip()
    if not token:
        sys.exit("Thiếu token: đặt biến CONFLUENCE_PAT hoặc tạo file ~/.confluence-pat")
    return token


def split_frontmatter(text):
    meta = {}
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            kv = re.match(r"^(\w+):\s*(.*)$", line)
            if kv:
                meta[kv.group(1)] = kv.group(2).strip().strip('"')
        text = text[m.end():]
    return meta, text


def to_storage(body_md):
    # Bỏ H1 đầu tiên vì Confluence đã hiển thị tiêu đề trang
    body_md = re.sub(r"^\s*# .*\n", "", body_md, count=1)
    # Python-Markdown khắt khe hơn GitHub: danh sách phải có dòng trống phía trước,
    # và danh sách con phải thụt 4 dấu cách
    lines, prev = [], ""
    for line in body_md.splitlines():
        m = re.match(r"^( +)([-*+] |\d+\. )", line)
        if m:
            line = " " * (len(m.group(1)) * 2) + line.lstrip(" ")
        is_item = re.match(r"^\s*([-*+] |\d+\. )", line)
        prev_is_item = re.match(r"^\s*([-*+] |\d+\. )", prev)
        if is_item and prev.strip() and not prev_is_item and not prev.startswith(">"):
            lines.append("")
        lines.append(line)
        prev = line
    body_md = "\n".join(lines)
    html = markdown.markdown(body_md, extensions=["tables", "fenced_code", "sane_lists"])
    # Storage format là XHTML: đóng các thẻ rỗng
    return re.sub(r"<(br|hr)>", r"<\1 />", html)


def find_page(session, title):
    r = session.get(f"{BASE_URL}/rest/api/content",
                    params={"spaceKey": SPACE_KEY, "title": title, "expand": "version"})
    r.raise_for_status()
    results = r.json().get("results", [])
    return results[0] if results else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--title", help="Tiêu đề trang (mặc định lấy title trong frontmatter)")
    ap.add_argument("--parent-id", help=f"Trang cha (mặc định {PARENT_ID} khi tạo mới; khi cập nhật thì giữ nguyên chỗ cũ)")
    ap.add_argument("--parent-title", help="Đặt dưới trang có tiêu đề này thay vì --parent-id")
    ap.add_argument("--dry-run", action="store_true", help="Chỉ in HTML, không gọi API")
    args = ap.parse_args()

    meta, body = split_frontmatter(Path(args.file).read_text(encoding="utf-8"))
    title = args.title or meta.get("title") or Path(args.file).stem
    storage = to_storage(body)

    if args.dry_run:
        print(f"Tiêu đề: {title}\n")
        print(storage)
        return

    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {load_token()}",
                            "Content-Type": "application/json"})

    parent_id = args.parent_id  # None = không chỉ định
    if args.parent_title:
        parent = find_page(session, args.parent_title)
        if not parent:
            sys.exit(f"Không tìm thấy trang cha: {args.parent_title}")
        parent_id = parent["id"]

    payload = {"type": "page", "title": title, "space": {"key": SPACE_KEY},
               "body": {"storage": {"value": storage, "representation": "storage"}}}

    existing = find_page(session, title)
    # Chỉ đổi trang cha khi được chỉ định rõ; cập nhật trang có sẵn thì giữ nguyên vị trí
    if parent_id or not existing:
        payload["ancestors"] = [{"id": parent_id or PARENT_ID}]
    if existing:
        payload["version"] = {"number": existing["version"]["number"] + 1}
        r = session.put(f"{BASE_URL}/rest/api/content/{existing['id']}", json=payload)
        action = "Đã cập nhật"
    else:
        r = session.post(f"{BASE_URL}/rest/api/content", json=payload)
        action = "Đã tạo"

    if not r.ok:
        sys.exit(f"Lỗi {r.status_code}: {r.text[:500]}")
    page = r.json()
    print(f"{action}: {BASE_URL}{page['_links']['webui']}")


if __name__ == "__main__":
    main()
