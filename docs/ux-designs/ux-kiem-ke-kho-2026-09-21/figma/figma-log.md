---
feature: kiem-ke-kho
wireframe: docs/ux-designs/ux-kiem-ke-kho-2026-09-21/wireframes/flow-kiem-ke-kho-2026-09-22.excalidraw
figma_file: EP (vẽ qua plugin Figma UI MCP Bridge — file chưa có link chia sẻ trong log)
figma_page: Kiểm kê kho
library: local (page Foundations của file EP)
mode: Đi kỹ
status: review
created: 22/09/2026
updated: 22/09/2026
---

# Figma log — Kiểm kê kho

## 1. Màn đã vẽ

| # | Frame | Trạng thái | Màn wireframe | Node id |
|---|---|---|---|---|
| 01 | Kiểm kê kho — Danh sách phiếu | Mặc định | ① | `1159:1292` |
| 01 | Kiểm kê kho — Danh sách phiếu | Trống | ① (thêm theo yêu cầu) | `1159:1667` |

Page `Page 1` có sẵn 2 frame `KK-01 Danh sách phiếu`, `KK-02 Chọn kho & sản phẩm` (không phải bản này vẽ) — **giữ nguyên, không sửa**.

## 2. Ánh xạ wireframe → component

| Màn | Phần tử wireframe | Component · variant | Ghi chú |
|---|---|---|---|
| ① | Thanh tiêu đề `Kiểm kê kho` | Page header: `Display/H5` | |
| ① | `+ Kiểm kê kho` (nền xám) | `Button/Primary/L`, icon Plus | Đặt ngoài cùng bên phải |
| ① | `Nhập Excel`, `Xuất Excel` | `Button/Secondary/L`, icon FileUp / FileDown | Đặt bên trái nút chính |
| ① | `01/09 – 22/09` | `Input/Date range` → `01/09/2026 – 22/09/2026` | Viết đủ năm |
| ① | `Nhập mã kiểm kho` | `Input/Search` (placeholder) | |
| ① | `Tìm` | `Button/Secondary/L`, không icon | |
| ① | `Lọc ▾` | `Select` (value `Lọc`) | |
| ① | Header bảng `Mã · Thời gian · Kho · Ghi chú · Trạng thái · (trống)` | Table header, cột cuối đặt tên `Thao tác` | Tên cột `Thao tác` do người dùng chốt |
| ① | `Chưa xử lý` / `Đã xử lý` | `Tag/Amber` / `Tag/Green` | |
| ① | `✎ 🗑` | `IconButton/Edit` + `IconButton/Delete` | Chỉ phiếu Chưa xử lý |
| ① | `🖨` | `IconButton/View` + `IconButton/Print` | Phiếu Đã xử lý: Xem + In (người dùng chốt; wireframe chỉ có In) |
| ① | Mã phiếu | Chữ `text/link` (bấm mở chi tiết) | |
| ① | `50 bản ghi/trang ‹ 1 2 3 ›` | `Select/S` + `1-12 of 12` + Pager | Xem [ASSUMPTION] 2 |
| ① | Chú thích xám `Phiếu Chưa xử lý: sửa / xóa được / Phiếu Đã xử lý: chỉ xem / in` | Không vẽ — chuyển sang mục 6 | Chú thích cho người đọc |

## 3. Chờ duyệt

Chưa có library EasyPOS nên **mọi component đều là bản dựng đầu tiên**, nằm ở page `Foundations`. Các mục dưới là phần suy ra (không có trong spec gốc), cần designer duyệt:

| Component | Dùng ở | Vì sao chưa có | Đề xuất |
|---|---|---|---|
| `Top bar/Quản lý` | Mọi trang quản lý | Spec gốc chỉ có top bar POS | Brand · nút `Bán hàng` · chuông + badge · tài khoản · menu |
| `Input/Date range` | Filter bar | Spec gốc chưa có date picker | Input + icon Calendar cuối |
| `Select/S` | Pager | Spec gốc chưa có | Select cao 32 |
| Page header, Filter bar, Data table, Empty state | Màn ① | Mẫu "Trang quản lý — danh sách" là suy ra | Theo `layouts.md` §2 |

## 4. Suy luận `[ASSUMPTION]`

| Chỗ | Suy luận | Căn cứ |
|---|---|---|
| 1. Mã phiếu dòng mẫu | Dùng KK012 → KK001, không đặt KK003/KK002/KK001 ở 3 dòng đầu như yêu cầu | Wireframe: KK003 ngày 22/09, KK001 ngày 01/09 đã phủ hết khoảng lọc 01/09–22/09 → không thể có thêm 9 dòng mới hơn KK003 hoặc cũ hơn KK001 trong cùng khoảng lọc. Nội dung 3 dòng wireframe giữ nguyên ở KK012 (22/09, Kiểm tháng 9, Chưa xử lý), KK007 (15/09, Nhóm sữa), KK001 (01/09, Kho 2) |
| 2. Pager | `1-12 of 12`, chỉ 1 trang, nút sau mờ | 12 dòng < 50 bản ghi/trang. Wireframe vẽ `‹ 1 2 3 ›` làm ví dụ |
| 3. Thời gian | `HH:mm DD/MM/YYYY`, vd `14:30 22/09/2026` | Wireframe chỉ ghi `22/09`; theo microcopy |
| 4. Sắp xếp | Mới nhất lên đầu theo Thời gian | Thứ tự dòng trên wireframe |
| 5. Thứ tự nút header | `Nhập Excel · Xuất Excel · + Kiểm kê kho` căn phải | Wireframe để nút chính trước, căn trái; quy tắc design system: nút chính ngoài cùng bên phải |
| 6. Frame Trống | Giữ filter bar và header bảng; thân bảng là khối trống + nút `Kiểm kê kho` | Yêu cầu người dùng; câu chữ tự viết: `Chưa có phiếu kiểm kê nào` / `Tạo phiếu kiểm kê để đối chiếu tồn kho thực tế với số liệu trên hệ thống` |

## 5. Câu hỏi mở

| Câu hỏi | Nguồn | Người trả lời | Trạng thái |
|---|---|---|---|
| Nút `Nhập Excel` giữ hay bỏ ở phase này? Hiện **đang giữ** theo wireframe | Ghi chú cam `BRIEF KHÁC: Nhập Excel làm ngay phase này (đặc tả để phase sau)` | PO | Mở |
| Ở frame Trống, `Xuất Excel` có nên disabled? | Suy luận khi vẽ | PO / designer | Mở |
| Mã phiếu dòng mẫu (xem [ASSUMPTION] 1) có chấp nhận không? | Yêu cầu vẽ | Người dùng | Mở |

## 6. Cho SRS

- Phiếu `Chưa xử lý`: được Sửa, Xóa. Phiếu `Đã xử lý`: chỉ Xem, In (chú thích wireframe + người dùng chốt thêm Xem).
- Bấm mã phiếu → mở chi tiết (màu link). Cần mô tả: phiếu Chưa xử lý mở lại Bước 2 (theo luồng `Sửa phiếu Chưa xử lý (✎) → mở lại Bước 2`).
- Bộ lọc: khoảng ngày (mặc định 01 của tháng → hôm nay — [ASSUMPTION] từ `01/09 – 22/09`), tìm theo mã phiếu, `Lọc` (nội dung dropdown chưa có trên wireframe — cần đặc tả: kho? trạng thái?).
- Phân trang: 50 bản ghi/trang.

## 7. Giới hạn kỹ thuật khi vẽ (plugin figma-ui-mcp 2.5.24, gói Starter)

- **Style chữ rác cần xóa tay** trong Figma (Assets → Local styles): `_t1`–`_t4` và các bản trùng tên `Display/H1`–`H6`, `Brand/Wordmark`, `Title/lg|md|sm|xs` loại **Inter 12 Regular**. Bản đúng là bản dùng Be Vietnam Pro / Noto Sans. Plugin không xóa được style.
- Weight SemiBold / ExtraBold được gắn qua variable chuỗi `font/weight-semibold`, `font/weight-extrabold` (collection `Typography`) vì plugin không nạp được tên style `SemiBold` của Noto Sans / Be Vietnam Pro trực tiếp.
- Số dùng Inter; chưa bật được tabular figures (plugin không có thuộc tính OpenType).
- Gói Starter tối đa 3 page → không có page `Chờ duyệt`; bản nháp để ở `Foundations`.
- Viền avatar trên top bar là hex `#FFFFFF80` chưa gắn variable.
- Icon: Lucide (thay Iconsax), dựng thành component theo cỡ `Icon/<cỡ>/<Tên>` vì instance không co giãn vector.

## 8. Lịch sử

| Ngày | Thay đổi | Người |
|---|---|---|
| 22/09/2026 | Dựng Foundations (variables, text styles, 29 icon, 17 component) và frame 01 Mặc định + Trống | Claude (easypos-design) |
