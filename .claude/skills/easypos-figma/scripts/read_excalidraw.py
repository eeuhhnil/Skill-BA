"""Tóm tắt wireframe Excalidraw thành danh sách màn, phần tử, luồng và ghi chú.

Dùng: python read_excalidraw.py <file.excalidraw> [--json]

Quy ước màu đọc theo references/excalidraw-mapping.md:
  #1e1e1e khung/chữ UI · #868e96 chữ UI phụ · #ced4da kẻ dòng
  #1971c2 nhãn luồng/hành động · #e67700 ghi chú (điểm chưa chốt)
"""
import json
import re
import sys

ROLE_BY_STROKE = {
    "#1971c2": "flow",
    "#e67700": "note",
    "#ced4da": "divider",
}
SCREEN_MIN_W, SCREEN_MIN_H = 300, 150
NUMBER_RE = re.compile(r"^\s*([①-⑳]|\d+)\s*([a-z])?\b")


def bbox(e):
    x, y, w, h = e["x"], e["y"], e["width"], e["height"]
    if w < 0:
        x, w = x + w, -w
    if h < 0:
        y, h = y + h, -h
    return x, y, w, h


def inside(inner, outer, tol=4):
    ix, iy, iw, ih = bbox(inner)
    ox, oy, ow, oh = bbox(outer)
    return ix >= ox - tol and iy >= oy - tol and ix + iw <= ox + ow + tol and iy + ih <= oy + oh + tol


def role(e):
    stroke = (e.get("strokeColor") or "").lower()
    bg = (e.get("backgroundColor") or "").lower()
    if stroke in ROLE_BY_STROKE:
        return ROLE_BY_STROKE[stroke]
    if bg == "#fff3bf":
        return "note"
    return "ui"


def text_of(e):
    return (e.get("text") or e.get("originalText") or "").strip()


def main(path, as_json=False):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    els = [e for e in data.get("elements", []) if not e.get("isDeleted")]
    by_id = {e["id"]: e for e in els}

    # Text bound to a container (rectangle label, arrow label).
    bound = {}
    for e in els:
        if e["type"] == "text" and e.get("containerId"):
            bound.setdefault(e["containerId"], []).append(text_of(e))

    shapes = [e for e in els if e["type"] in ("rectangle", "frame", "ellipse", "diamond")]
    big = [e for e in shapes if bbox(e)[2] >= SCREEN_MIN_W and bbox(e)[3] >= SCREEN_MIN_H]
    # Screens = large shapes not nested inside another large shape (frames always count).
    screens = [e for e in big if e["type"] == "frame" or not any(o is not e and inside(e, o) for o in big)]
    screens.sort(key=lambda e: (round(bbox(e)[1] / 200), bbox(e)[0]))

    def owner(e):
        for s in screens:
            if s is not e and inside(e, s):
                return s["id"]
        # Title text sitting just above a screen belongs to it.
        if e["type"] == "text":
            x, y, w, h = bbox(e)
            for s in screens:
                sx, sy, sw, sh = bbox(s)
                if sx - 4 <= x <= sx + sw and sy - 60 <= y + h <= sy + 4:
                    return s["id"]
        return None

    out_screens = []
    for s in screens:
        sx, sy, sw, sh = bbox(s)
        items = []
        for e in els:
            if e is s or e["type"] in ("arrow", "line") or e.get("containerId"):
                continue
            if owner(e) != s["id"]:
                continue
            x, y, w, h = bbox(e)
            item = {
                "id": e["id"],
                "type": e["type"],
                "role": role(e),
                "x": round(x - sx), "y": round(y - sy), "w": round(w), "h": round(h),
            }
            if e["type"] == "text":
                item["text"] = text_of(e)
            elif e["id"] in bound:
                item["label"] = " / ".join(bound[e["id"]])
            if (e.get("backgroundColor") or "transparent") != "transparent":
                item["fill"] = e["backgroundColor"]
            items.append(item)
        items = [i for i in items if not (i["type"] == "text" and not i.get("text"))]
        # A small shape holding exactly one text = one control (button, input, select).
        merged = set()
        for i in items:
            if i["type"] == "text" or i.get("label") or i["h"] > 44:
                continue
            inner = [t for t in items if t["type"] == "text" and t["id"] not in merged
                     and t["x"] >= i["x"] - 2 and t["y"] >= i["y"] - 2
                     and t["x"] + t["w"] <= i["x"] + i["w"] + 2 and t["y"] + t["h"] <= i["y"] + i["h"] + 2]
            if len(inner) == 1:
                i["label"] = inner[0]["text"]
                i["type"] = "control"
                merged.add(inner[0]["id"])
        items = [i for i in items if i["id"] not in merged]
        items.sort(key=lambda i: (i["y"] // 12, i["x"]))
        texts = [i for i in items if i.get("text")]
        title = s.get("name") or next((i["text"] for i in texts if NUMBER_RE.match(i["text"])), None)
        if not title and texts:
            title = texts[0]["text"]
        out_screens.append({
            "id": s["id"], "title": (title or "").replace("\n", " "),
            "x": round(sx), "y": round(sy), "w": round(sw), "h": round(sh),
            "items": items,
        })

    titles = {s["id"]: s["title"] for s in out_screens}

    def locate(elem_id):
        e = by_id.get(elem_id)
        if not e:
            return None
        if e["id"] in titles:
            return titles[e["id"]]
        o = owner(e)
        return titles.get(o) if o else None

    def dist_to(px, py, s):
        sx, sy, sw, sh = bbox(s)
        dx = max(sx - px, 0, px - (sx + sw))
        dy = max(sy - py, 0, py - (sy + sh))
        return (dx * dx + dy * dy) ** 0.5

    def nearest_screen(px, py, limit=160):
        best = min(screens, key=lambda s: dist_to(px, py, s), default=None)
        return titles[best["id"]] if best is not None and dist_to(px, py, best) <= limit else None

    # Flow labels drawn as free text (blue) outside any screen.
    free_texts = [e for e in els if e["type"] == "text" and not e.get("containerId")
                  and role(e) == "flow" and owner(e) is None]
    used_labels = set()

    flows = []
    for e in els:
        if e["type"] != "arrow":
            continue
        pts = e.get("points") or [[0, 0], [e["width"], e["height"]]]
        p0 = (e["x"] + pts[0][0], e["y"] + pts[0][1])
        p1 = (e["x"] + pts[-1][0], e["y"] + pts[-1][1])
        start = (e.get("startBinding") or {}).get("elementId")
        end = (e.get("endBinding") or {}).get("elementId")
        label = " / ".join(bound.get(e["id"], []))
        if not label and free_texts:
            # Nearest free blue text to any point of the arrow.
            apts = [(e["x"] + p[0], e["y"] + p[1]) for p in pts]
            def d(t):
                tx, ty, tw, th = bbox(t)
                cx, cy = tx + tw / 2, ty + th / 2
                return min(((cx - ax) ** 2 + (cy - ay) ** 2) ** 0.5 for ax, ay in apts)
            cand = min((t for t in free_texts if t["id"] not in used_labels), key=d, default=None)
            if cand is not None and d(cand) <= 220:
                label = text_of(cand)
                used_labels.add(cand["id"])
        flows.append({
            "id": e["id"],
            "from": (locate(start) if start else None) or nearest_screen(*p0),
            "from_element": (text_of(by_id[start]) or " / ".join(bound.get(start, []))) if start in by_id else None,
            "to": (locate(end) if end else None) or nearest_screen(*p1),
            "label": label,
        })

    free_flow = [text_of(t) for t in free_texts if t["id"] not in used_labels]

    def note_near(e):
        x, y, w, h = bbox(e)
        return locate(e["id"]) or nearest_screen(x + w / 2, y + h / 2, limit=400)

    notes = [{"text": text_of(e), "near": note_near(e)} for e in els
             if e["type"] == "text" and role(e) == "note"]

    result = {"file": path, "screens": out_screens, "flows": flows,
              "flow_labels_unbound": free_flow, "notes": notes}
    if as_json:
        print(json.dumps(result, ensure_ascii=False, indent=1))
        return

    print(f"# Wireframe: {path}\n")
    print(f"{len(out_screens)} màn · {len(flows)} mũi tên · {len(notes)} ghi chú\n")
    for s in out_screens:
        print(f"## {s['title'] or '(chưa có tiêu đề)'}  [{s['w']}×{s['h']} @ {s['x']},{s['y']}]")
        for i in s["items"]:
            desc = i.get("text") or i.get("label") or ""
            desc = desc.replace("\n", " / ")
            fill = f" fill={i['fill']}" if i.get("fill") else ""
            print(f"- ({i['x']},{i['y']} {i['w']}×{i['h']}) {i['type']}:{i['role']}{fill} {desc}".rstrip())
        print()
    if flows:
        print("## Luồng")
        for f in flows:
            src = f["from"] or "?"
            if f["from_element"]:
                src += f" [{f['from_element'].replace(chr(10), ' ')}]"
            label = f["label"].replace("\n", " ")
            print(f"- {src} → {f['to'] or '?'}" + (f"  «{label}»" if label else ""))
        print()
    if free_flow:
        print("## Nhãn luồng không gắn mũi tên")
        for t in free_flow:
            print("- " + t.replace("\n", " / "))
        print()
    if notes:
        print("## Ghi chú (điểm chưa chốt)")
        for n in notes:
            print(f"- [{n['near'] or 'ngoài màn'}] " + n["text"].replace("\n", " / "))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    main(args[0], as_json="--json" in sys.argv)
