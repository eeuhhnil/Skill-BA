# Vẽ bằng plugin Figma UI MCP Bridge (`figma-ui-mcp`)

Dùng khi công cụ vẽ là `mcp__figma-ui__*` thay cho `use_figma`. Plugin vẽ vào file đang mở trong Figma; không cần link. Đã kiểm với plugin 2.5.24.

## Trước khi vẽ
1. `figma_status` → kiểm `pluginConnected`, tên file, số page. Nhiều tab → ghim `sessionId`.
2. `figma_docs` (không section), rồi `api`, `tokens`, `layout`, `icons` khi cần.
3. `figma_read get_page_nodes`, `get_variables`, `get_styles`, `get_local_components` → biết file đã có gì. Không sửa frame có sẵn.
4. Đọc bảng ID Foundations của file (vd `docs/ux-designs/_figma-EP-foundations.md`) — mỗi lần `figma_write` là sandbox mới, phải khai lại ID.

## Bẫy đã gặp và cách xử lý

| Vấn đề | Cách làm đúng |
|---|---|
| `create TEXT` luôn dùng Inter, bỏ qua `fontFamily` | Tạo text → `applyTextStyle({ nodeId, styleId })` |
| Text bị khung cố định 100×100 | Sau khi áp style: `modify({ id, textAutoResize: "WIDTH_AND_HEIGHT", layoutSizingHorizontal: "HUG", layoutSizingVertical: "HUG" })`; text co giãn theo cột: `textAutoResize: "HEIGHT", layoutSizingHorizontal: "FILL"` |
| `applyTextStyle({ styleName })` chọn style đầu tiên trùng tên | Luôn truyền `styleId` |
| Weight `SemiBold`/`ExtraBold` bị đổi thành `Semi Bold` (tên của Inter) → Noto Sans / Be Vietnam Pro lỗi font | `setupDesignTokens({ collectionName: "Typography", fonts: { "font/weight-semibold": "SemiBold" }, textStyles: { "Title/md": { fontWeight: "{font/weight-semibold}", … } } })` — style được gắn variable chuỗi, Figma tự đọc đúng |
| `createTextStyle` lỗi font vẫn để lại style rác | Thử trên 1 style trước; plugin không xóa được style → báo người dùng xóa tay |
| Alias variable | `createVariable({ value: { type: "VARIABLE_ALIAS", id } })` hoạt động |
| Màu có alpha | Tạo xong gọi `modifyVariable({ variableName, value: "#FFFFFF29" })` |
| Icon SVG | `create({ type: "SVG", svg })` → `flatten` (frame bị mất, còn vector) → tạo frame cỡ icon → `append({ parentId, childId })` → `modify` x/y về tọa độ trong frame → `applyVariable` stroke → `createComponent` |
| Instance icon không co giãn vector khi resize | Tạo component theo từng cỡ `Icon/24|20|18|16|48/<Tên>`; SVG scale làm nét mỏng đi → đặt `stroke-width = 1.5 × 24 / cỡ` hoặc `modify strokeWeight` sau khi flatten |
| Đổi màu icon trong instance | `applyVariable({ nodeId: "I<instance>;<vector master>", field: "stroke", variableName })`; lồng nhiều cấp: `I<a>;<b>;<c>` |
| Swap `INSTANCE_SWAP` sang đúng component đang có | Reset override màu → gắn lại màu sau khi swap |
| `figma_read screenshot` trả nhầm node ở page khác | `setPage` + `set_selection` + `set_viewport` trong `figma_write` trước khi chụp |
| Gói Starter | Tối đa 3 page: dùng `Page 1` (giữ nguyên) · `Foundations` · page nghiệp vụ; bản nháp `_draft/*` để trong `Foundations` |
| `counterAxisAlignItems: "STRETCH"` | Không hợp lệ; dùng `"MIN"` + con `layoutSizingHorizontal: "FILL"` |
| Viền một cạnh | Không có; dùng khung ngang `[nội dung | RECTANGLE 1px FILL]` hoặc divider RECTANGLE trong auto layout dọc |

## Nhịp làm
- Mỗi `figma_write` dựng một vùng (≤ ~150 thao tác, ~1 phút). Bảng nhiều dòng: chia 6 dòng/lần.
- Chụp sau mỗi vùng; chụp cả frame ở scale 0.5–0.6 trước khi báo xong.
- Ghi ID component mới vào bảng ID Foundations ngay khi tạo.
