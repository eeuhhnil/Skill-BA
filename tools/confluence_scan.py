# /// script
# dependencies = ["requests"]
# ///
"""Tìm và đọc trang trên Confluence Data Center (chỉ đọc) phục vụ phân tích ảnh hưởng.

Token: Personal Access Token của Confluence, đọc từ biến môi trường CONFLUENCE_PAT
hoặc từ file ~/.confluence-pat (một dòng, chỉ chứa token).

Hai lệnh con:
  search  Tìm theo từ khóa trong một space, gộp và xếp hạng trang theo số từ khóa khớp.
  fetch   Tải nội dung trang về dạng text; --grep chỉ giữ đoạn chứa từ khóa (±1 dòng).

Ví dụ:
  uv run tools/confluence_scan.py search --kw "kiểm kê" --kw "tồn kho" --skip TestCase --out rank.json
  uv run tools/confluence_scan.py fetch 50698190 50698161 --out-dir pages
  uv run tools/confluence_scan.py fetch 50698161 --out-dir pages --grep "tồn kho|giá vốn"
"""
import argparse
import html
import json
import os
import re
import sys
from pathlib import Path

import requests

BASE_URL = "https://confluence-sds.softdreams.vn:8090"
SPACE_KEY = "EP"


def load_token():
    token = os.environ.get("CONFLUENCE_PAT")
    if not token:
        token_file = Path.home() / ".confluence-pat"
        if token_file.exists():
            token = token_file.read_text(encoding="utf-8").strip()
    if not token:
        sys.exit("Thiếu token: đặt biến CONFLUENCE_PAT hoặc tạo file ~/.confluence-pat")
    return token


def session():
    s = requests.Session()
    s.headers.update({"Authorization": f"Bearer {load_token()}"})
    return s


def search(s, keywords, space, skip, out):
    pages = {}
    for kw in keywords:
        start = 0
        while True:
            r = s.get(f"{BASE_URL}/rest/api/content/search", timeout=60, params={
                "cql": f'space={space} and type=page and text ~ "\\"{kw}\\""',
                "limit": 100, "start": start, "expand": "ancestors"})
            r.raise_for_status()
            results = r.json().get("results", [])
            for p in results:
                ancestors = [a["title"] for a in p["ancestors"]]
                if set(skip) & (set(ancestors) | {p["title"]}):
                    continue
                d = pages.setdefault(p["id"], {"id": p["id"], "title": p["title"],
                                               "path": " > ".join(ancestors), "keywords": []})
                d["keywords"].append(kw)
            if len(results) < 100:
                break
            start += 100
    ranked = sorted(pages.values(), key=lambda p: -len(p["keywords"]))
    Path(out).write_text(json.dumps(ranked, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(ranked)} trang → {out}")
    for p in ranked[:40]:
        print(f'{len(p["keywords"]):>2}  {p["id"]}  {p["path"][-45:]} | {p["title"]}')


def to_text(storage):
    s = re.sub(r"</(p|h\d|li|tr|div)>", "\n", storage)
    s = re.sub(r"<(td|th)[^>]*>", " | ", s)
    s = re.sub(r"<h(\d)[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", s)
    s = re.sub(r"<li[^>]*>", "- ", s)
    s = html.unescape(re.sub(r"<[^>]+>", "", s))
    return re.sub(r"\n\s*\n+", "\n", s)


def fetch(s, ids, out_dir, grep):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pattern = re.compile(grep, re.I) if grep else None
    for pid in ids:
        j = s.get(f"{BASE_URL}/rest/api/content/{pid}", timeout=60,
                  params={"expand": "body.storage,version,history.lastUpdated,ancestors"}).json()
        last = j["history"]["lastUpdated"]
        header = (f"=== {j['title']} | id {pid} | v{j['version']['number']} | "
                  f"sửa {last['when'][:10]} bởi {last['by'].get('displayName')} | "
                  f"{BASE_URL}/pages/viewpage.action?pageId={pid}")
        lines = to_text(j["body"]["storage"]["value"]).splitlines()
        if pattern:
            keep = set()
            for i, line in enumerate(lines):
                if pattern.search(line):
                    keep |= {i - 1, i, i + 1}
            lines = [lines[i][:400] for i in sorted(keep) if 0 <= i < len(lines)]
        (out / f"{pid}.txt").write_text(header + "\n" + "\n".join(lines), encoding="utf-8")
        print(f"{pid}  {len(lines)} dòng  {j['title']}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("search")
    a.add_argument("--kw", action="append", required=True)
    a.add_argument("--space", default=SPACE_KEY)
    a.add_argument("--skip", action="append", default=[], help="Bỏ trang có tổ tiên mang tên này")
    a.add_argument("--out", default="rank.json")
    b = sub.add_parser("fetch")
    b.add_argument("ids", nargs="+")
    b.add_argument("--out-dir", default="pages")
    b.add_argument("--grep", help="Regex; chỉ giữ dòng khớp ±1 dòng")
    args = ap.parse_args()

    s = session()
    if args.cmd == "search":
        search(s, args.kw, args.space, args.skip, args.out)
    else:
        fetch(s, args.ids, args.out_dir, args.grep)


if __name__ == "__main__":
    sys.exit(main())
