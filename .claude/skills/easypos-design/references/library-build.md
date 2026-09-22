# Dựng EasyPOS Library trên Figma

Library là bản dựng từ `tokens.md` + `components.md`. **Skill là nguồn gốc**: có thay đổi thì sửa file tham chiếu trước, rồi mới cập nhật library.

Trước khi làm: nạp `/figma-use` và `figma-generate-library`. Cần một file Figma người dùng có quyền edit. Tên file gợi ý: `EasyPOS – Library`.

## 1. Cấu trúc page

| Page | Nội dung |
|---|---|
| `Cover` | Tên, phiên bản, ngày cập nhật, link về skill |
| `Foundations` | Bảng màu, thang chữ, radius, spacing, shadow (frame minh họa, gắn variable) |
| `Icons` | Component `Icon/<Tên>` 24×24 |
| `Components` | Component cơ bản (components.md §1) |
| `POS` | Khung POS (§2) |
| `Overlays` | Modal, Payment modal, Toast, Confirm dialog (§3) |
| `Management` | Thành phần trang quản lý (§4) — đánh dấu `[suy ra]` trên frame |
| `Templates` | Frame mẫu 1920×1080 cho từng mẫu trang trong `layouts.md` |
| `Chờ duyệt` | Bản nháp `_draft/*` do các lần vẽ màn đề xuất |

## 2. Trình tự dựng

Làm tuần tự, mỗi bước một hoặc vài lần gọi `use_figma`, chụp màn kiểm tra sau mỗi bước.

1. **Variables**
   - Collection `Primitives` (mode `Light`): toàn bộ màu `tokens.md` §1. Nhóm bằng dấu `/` (`blue/500`). Ẩn khỏi publishing (scope rỗng) để người vẽ dùng semantic.
   - Collection `Semantic` (mode `Light`): `tokens.md` §2, **alias** sang Primitives. Đặt scope phù hợp (text/* → Text fill; surface/* → Frame fill; border/* → Stroke).
   - Collection `Radius`, `Spacing`: kiểu number, scope Corner radius / Gap + Padding.
   - Đặt code syntax (Web) cho từng variable: `var(--blue-500)`… để dev inspect thấy tên CSS.
2. **Text styles** theo `tokens.md` §3. Nạp font trước. Style `Number/*` bật tabular figures.
3. **Effect styles** theo `tokens.md` §7.
4. **Icons** (xem §3 dưới).
5. **Components cơ bản**, theo thứ tự phụ thuộc: Keycap → Button → Input → Select → Search field → Checkbox/Radio/Toggle → Tag → Status dot → Count badge → Chip → Segmented → Tabs → Stepper số lượng → Pager → Avatar → Tooltip.
6. **POS**: Top bar → Rail → Order header → Cart row + Add-on row → Cart table → Product card → Product picker → Bottom bar.
7. **Overlays**, rồi **Management**.
8. **Templates**: ghép từ instance, đúng số đo `layouts.md`.
9. **Foundations**: frame minh họa.
10. **Cover**, rồi nhắc người dùng **Publish** (Assets → Publish). Không tự publish.

## 3. Icon

- `{workflow.icon_source}` = `lucide-svg`: tải SVG về scratchpad, vd
  `curl -s https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/<kebab-name>.svg -o <scratchpad>/icons/<kebab-name>.svg`,
  rồi đưa nội dung SVG vào `figma.createNodeFromSvg()` trong `use_figma`. Đổi stroke thành 1.5, màu stroke gắn `text/primary` (instance đổi màu được), khung 24×24, đổi thành component `Icon/<PascalName>`.
- Danh sách tối thiểu: toàn bộ icon trong `components.md` và bảng emoji của `excalidraw-mapping.md`.
- Sản phẩm thật dùng **Iconsax**. Khi có bộ Iconsax chính thức, thay SVG trong component `Icon/*` (giữ tên) — mọi màn tự cập nhật.

## 4. Quy tắc cho component

- Auto layout cho mọi component; padding/gap gắn variable `Spacing`; radius gắn `Radius`; màu gắn `Semantic`.
- Variant đặt tên `Thuộc tính=Giá trị` đúng như cột **Figma** trong `components.md`. Chữ đổi được dùng text property; icon đổi được dùng instance swap với preferred values là các `Icon/*`.
- Mỗi component có mô tả ngắn (dùng khi nào, không dùng khi nào) và link về mục tương ứng trong `components.md`.
- Component có nhãn `[suy ra]` thêm dấu `◇` ở cuối tên hiển thị trong mô tả để designer biết cần duyệt; khi đã duyệt thì bỏ nhãn trong `components.md` và trong mô tả.

## 5. Bản nháp từ lần vẽ màn

Page `Chờ duyệt` gom các `_draft/*`. Khi người dùng duyệt một bản nháp:
1. Thêm spec vào `components.md` (hỏi người dùng trước khi sửa skill).
2. Chuyển component sang page phù hợp, bỏ tiền tố `_draft/`.
3. Publish lại library.

## 6. Cập nhật library

Khi token hoặc spec đổi: sửa file tham chiếu → sửa variable/component tương ứng (không tạo mới) → ghi phiên bản mới trên `Cover` → nhắc người dùng publish và các file đang dùng bấm **Accept updates**.
