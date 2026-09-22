# Thay đổi so với bản skill gốc (easypos-skill-figma-make.md)

Bản gốc viết cho Figma Make (xuất code React/CSS). Bản này viết lại để **vẽ trực tiếp lên Figma** từ wireframe Excalidraw. Các số đo dưới đây đã được chuẩn hóa theo chính quy tắc của bản gốc (thang radius 4/6/8/12/16, lưới 4px). **Cần designer xác nhận**; nếu sản phẩm thật dùng số cũ thì trả lại số cũ trong `tokens.md` / `components.md` và ghi vào đây.

## Cấu trúc
- Bỏ phần code CSS và React (§5, §6 bản gốc); số đo được chuyển vào `components.md` và `layouts.md`.
- Bỏ hướng dẫn Figma Make (§0 bản gốc); thay bằng quy trình Excalidraw → Figma trong `SKILL.md`.
- Thêm tên Figma variable/style cho mọi token.
- Thêm mẫu trang quản lý, component trang quản lý, confirm dialog, toast lỗi, date picker, tooltip — đánh dấu `[suy ra]`.
- Thêm script đọc Excalidraw và quy tắc chuyển phần tử sang component.

## Mâu thuẫn trong bản gốc đã sửa

| Chỗ | Bản gốc | Bản này | Lý do |
|---|---|---|---|
| Radius mục rail | quy tắc 8, CSS 10 | 8 | theo quy tắc |
| Radius segmented, chế độ bán, bảng giá, nút header | 9 / 7 | 8 (vỏ) · 6 (nút trong segmented) | ngoài thang |
| Radius ô tổng tiền, input popup, phương thức thanh toán, toast, nút Hoàn thành | 10 | 8 | ngoài thang |
| Radius chip lọc, nút pager | 7 | 6 | ngoài thang |
| Radius tag | 5 | 6 | ngoài thang |
| Radius nút Lưu đơn / Thanh toán | quy tắc 6, CSS 8 | 8 | nút lớn, giữ theo CSS |
| Count badge | quy tắc cao 18 radius 999; QR order cao 22 radius 6 | cao 20, radius full, 2 tone Red/Orange | thống nhất một component |
| Chấm tồn kho trên product card | luôn xanh dương | theo trạng thái xanh lá / vàng / đỏ | theo quy tắc status dot |
| Toast cảnh báo | chữ trắng trên `#F0A92A` (tương phản ~2:1) | chữ `ink` trên `#F0A92A` | đủ tương phản |
| Icon dòng topping | luôn `Gift` | `CirclePlus` | phân biệt với quà tặng |
| Hex trần trong CSS | `#dcebf6`, `#cfd6de`, `#0a1726` | `blue/150` thành token; hai màu còn lại chỉ dùng cho code preview, bỏ | quy tắc không hex trần |
| Icon Báo cáo | `BarChart3` ("đổi tên") | `ChartColumn` | tên hiện tại của Lucide |
| Font số | SF Pro Display / `-apple-system` | `{workflow.number_font}`, mặc định Inter tabular | SF Pro không có trên Windows / Figma web |

## Số đo chuẩn hóa theo lưới 4px

| Chỗ | Bản gốc | Bản này |
|---|---|---|
| Padding main, rail, order header | 14 | 16 |
| Ô tìm kiếm, nút lọc | cao 42 | 40 |
| Chế độ bán, bảng giá, nút header | cao 46 | 48 |
| Pager | 30 | 32 |
| Cột Đơn giá / Thành tiền | 110 / 130 | 112 / 128 |
| Thumbnail product card | 62 | 64 |
| Padding product card | 10 | 12 |
| Bottom bar | 160 (gồm padding 14 + 16) | 128 nội dung, khoảng cách lấy từ gap của main |
| Các gap 7 / 9 / 11 / 13 | | 8 / 8 / 12 / 12 |
| Top bar 70, rail 72, canvas 1920×1080 | giữ nguyên | kích thước khung sản phẩm |

## Chưa giải quyết (cần nguồn)
- Logo chính thức (hiện là bản dựng lại).
- Bộ icon Iconsax chính thức.
- Spec thật cho màn F&B, Khách sạn, trang quản lý.
- Dark mode: bản gốc không có, bản này cũng không làm.
