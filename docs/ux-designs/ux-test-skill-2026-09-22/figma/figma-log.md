---
feature: quan-ly-ca-ket-ca
wireframe: docs/ux-designs/ux-test-skill-2026-09-22/.working/flow-quan-ly-tra-cuu-ca-2026-09-22.excalidraw
figma_file: https://www.figma.com/design/h4T7Q4qOWSHLyHXdSH3o45/EP
figma_page: https://www.figma.com/design/h4T7Q4qOWSHLyHXdSH3o45/EP?node-id=1165-833
library: local (file EP đã có sẵn Design system nội bộ, page "Design system")
mode: Đi nhanh (1 màn, vẽ thử)
status: draft
created: 22/09/2026
updated: 22/09/2026
---

# Figma log — Quản lý ca, kết ca

## 1. Màn đã vẽ

| # | Frame | Trạng thái | Màn wireframe | Link (node id) |
|---|---|---|---|---|
| 01 | QLC-01 · Danh sách ca làm việc | Mặc định | Screen 1 của flow-quan-ly-tra-cuu-ca | `1165:833` |

Chỉ vẽ màn "Danh sách ca làm việc" (Screen 1) theo yêu cầu — chưa vẽ Screen 2 "Chi tiết ca" của cùng file wireframe.

## 2. Ánh xạ wireframe → component

| Màn | Phần tử wireframe | Component · variant | Ghi chú |
|---|---|---|---|
| 01 | Tiêu đề "Danh sách ca làm việc" | Text style `Display/H5` | |
| 01 | Filter "Khoảng thời gian" | `Input/Date range` | Dùng giá trị mặc định của component |
| 01 | Filter "Trạng thái / (Đang mở / Đã đóng)" | `Select`, Value = "Trạng thái" | Hiển thị dạng placeholder, chưa mở danh sách lựa chọn |
| 01 | Filter "Nhân viên" | `Select`, Value = "Nhân viên" | Như trên |
| 01 | Nút "Lọc" | `Button/Secondary/L`, Label = "Lọc", tắt Leading icon | |
| 01 | Bảng 7 cột (Nhân viên, Giờ mở ca, Giờ đóng ca, Tiền đầu ca, Tiền kết ca, Chênh lệch, Trạng thái) | `Data table` (dựng theo `layouts.md`/`components.md` §Data table — chưa có component Table đóng gói sẵn trong library) | Header 48, dòng 56, đúng theo spec |
| 01 | Cột số (Tiền đầu ca/kết ca/Chênh lệch) | Text style số kiểu `Number/table` (Inter Bold 15, căn phải) | |
| 01 | Chênh lệch của Lan có dấu `(!)` | Chữ số tô đỏ `error/500` + đậm khi khác 0đ | Thay cho icon cảnh báo — xem mục 4 |
| 01 | Trạng thái "Đã đóng" | `Tag/Green`, Label = "Đã đóng" | Tái dùng đúng component có sẵn |
| 01 | Trạng thái "Đang mở" | `_draft/Tag-Blue · Đang mở` (bản nháp) | Chưa có Tag tone Blue trong library — xem mục 3 |
| 01 | Top bar | Instance `Top bar/Quản lý` | Dùng nguyên component có sẵn |
| 01 | Sidebar | Instance `Rail` | Không có mục "Quản lý ca" trong danh sách rail hiện có — xem mục 5 |

## 3. Chờ duyệt (bản nháp `_draft/*`)

| Component | Dùng ở | Vì sao chưa có trong library | Đề xuất |
|---|---|---|---|
| `_draft/Tag-Blue · Đang mở` (2 instance, không phải component thật — dựng tay theo đúng cấu trúc Tag) | Cột Trạng thái, dòng Tuấn và Quân | `components.md` có định nghĩa tone Blue (`blue/100` nền, `blue/700` chữ) nhưng file EP hiện chỉ có `Tag/Amber` và `Tag/Green` được dựng thành component thật | Dựng thành `Tag/Blue` component thật trong page "Design system" nếu chốt dùng tone Blue cho trạng thái "Đang mở" (xem câu hỏi mở #2) |

## 4. Suy luận `[ASSUMPTION]`

| Chỗ | Suy luận | Căn cứ |
|---|---|---|
| Mẫu trang dùng cho màn này | Dùng mẫu "2. Trang quản lý — danh sách" trong `layouts.md` — mẫu này tự ghi là `[suy ra]`, chưa được designer xác nhận trong bản gốc | `layouts.md` §2 |
| Chênh lệch ≠ 0 tô đỏ đậm thay vì icon cảnh báo `(!)` như wireframe | Tái dùng token màu `error/500` có sẵn thay vì dựng icon `AlertCircle`/`TriangleAlert` mới (icon này chưa có trong 50 component hiện có của file) | Ưu tiên tái dùng thay vì dựng bản nháp mới khi có thể |
| Trạng thái "Đang mở" dùng tone Blue | Không có tiền lệ trực tiếp trong `components.md`; chọn Blue vì gần nghĩa "đang diễn ra/thông tin trung tính" nhất trong bảng tone Tag hiện có | `components.md` bảng Tag |
| Rail active = không có mục nào sáng | "Quản lý ca" không khớp 12 mục rail hiện có (Bán hàng, Đơn hàng, Sản phẩm, Đơn lưu, Khuyến mãi, Khách hàng, Kho, Giao dịch, Báo cáo, Sổ quỹ, Trang chủ, Cài đặt) | `components.md` §Left rail |
| Không vẽ Pager ở cuối bảng | Mẫu trang quản lý-danh sách có Pager theo `layouts.md`, nhưng wireframe gốc không có phần tử Pager nào ở Screen 1 — ưu tiên đúng theo wireframe | `read_excalidraw.py` output của Screen 1 không có Pager |
| Không vẽ trạng thái Trống / Đang lọc | Wireframe chỉ có 1 trạng thái (Mặc định, có dữ liệu); người dùng yêu cầu "vẽ thử" 1 màn | Phạm vi yêu cầu của người dùng trong phiên này |

## 5. Câu hỏi mở

| Câu hỏi | Nguồn (ghi chú / wireframe) | Người trả lời | Trạng thái |
|---|---|---|---|
| "Quản lý ca" có cần một mục riêng trên Rail (sidebar), hay nằm lồng trong "Sổ quỹ"? | Không có mục rail nào khớp | Designer/PO | [ ] |
| Trạng thái "Đang mở" nên dùng tone màu nào cho Tag — Blue (đề xuất tạm) hay tone khác? | Không có tiền lệ trong `components.md` | Designer | [ ] |
| Bảng có cần Pager (phân trang) không nếu số ca trong ngày nhiều? | Wireframe gốc không vẽ Pager | PO/BA | [ ] |
| Dấu hiệu chênh lệch `(!)` trên wireframe — chỉ cần tô đỏ số như đã vẽ, hay cần thêm icon cảnh báo riêng (phải dựng `_draft` icon mới vì chưa có trong library)? | Wireframe có emoji `(!)` cạnh số chênh lệch | Designer | [ ] |

## 6. Cho SRS

- Cột "Chênh lệch" trong bảng: giá trị khác 0đ hiển thị màu đỏ đậm (khác biệt trực quan so với dòng khớp quỹ) — quy tắc hiển thị cần đưa vào SRS.
- Cột "Trạng thái": 2 giá trị "Đang mở" / "Đã đóng", mỗi giá trị một màu Tag riêng — cần chốt bảng màu chính thức trước khi đưa vào SRS (xem câu hỏi mở #2).
- Bộ lọc gồm 3 trường (Khoảng thời gian, Trạng thái, Nhân viên) + nút Lọc riêng (không lọc tự động khi đổi Select) — hành vi lọc cần mô tả rõ trong SRS (bấm Lọc mới áp dụng, hay lọc live?).
- Toàn bộ dòng trong bảng có thể bấm vào để mở "Chi tiết ca" (theo ghi chú trên wireframe) — chưa vẽ màn đích (Screen 2) trong phiên này.

## 7. Lịch sử

| Ngày | Thay đổi | Người |
|---|---|---|
| 22/09/2026 | Vẽ thử màn "Danh sách ca làm việc" (Đi nhanh, 1 màn) | easypos-design |
