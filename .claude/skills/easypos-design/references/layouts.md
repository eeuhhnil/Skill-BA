# Mẫu trang EasyPOS

Mọi màn desktop là frame **1920×1080**, nền `surface/page`, không có thanh cuộn ngoài. Chỉ phần thân bảng/lưới được cuộn bên trong: khi vẽ, đặt `clip content` cho vùng cuộn và để dữ liệu mẫu vừa khung hoặc tràn nhẹ ở đáy.

Mỗi màn thuộc một trong các mẫu dưới. Không khớp mẫu nào → báo người dùng, dùng **Đi kỹ**, ghi `[ASSUMPTION]`.

---

## 1. Bán hàng (POS)

Đã đối chiếu với sản phẩm thật. Dùng cho Bán hàng bán lẻ, và làm nền cho F&B, Khách sạn.

```
1920 ┌──────────────────────────────────────────────────────────────────┐
  70 │ TOP BAR                                                          │
     ├────┬─────────────────────────────────────────────────────────────┤
     │RAIL│ padding 16                                                   │
     │ 72 │ ORDER HEADER                                           h 48 │
     │    │ gap 16                                                       │
     │    │ CART  1096 × 770            │16│ PICKER  704 × 770          │
     │    │ gap 16                                                       │
     │    │ BOTTOM LEFT 1096 × 128      │16│ ACTIONS 704 × 128          │
     │    │ padding 16                                                   │
1080 └────┴─────────────────────────────────────────────────────────────┘
```

| Vùng | Kích thước | Ghi chú |
|---|---|---|
| Top bar | 1920 × 70 | Component `POS/Top bar` |
| Body | 1920 × 1010 | Ngang: rail + main |
| Rail | 72 × 1010 | `POS/Rail`, mục active = `Bán hàng` |
| Main | 1848 × 1010 | Dọc, padding 16, gap 16; bề rộng trong 1816 |
| Order header | 1816 × 48 | `POS/Order header` |
| Vùng làm việc | 1816 × 770 | Ngang, gap 16; tỉ lệ cart : picker = 1,55 : 1 |
| Cart | 1096 × 770 | `POS/Cart table`; cột tên sản phẩm = 504 |
| Picker | 704 × 770 | `POS/Product picker`; product card rộng 326 (2 cột) |
| Bottom bar | 1816 × 128 | Trái 1096, phải 704 (Lưu đơn 324, Thanh toán 364) |

Tổng dọc main: 16 + 48 + 16 + 770 + 16 + 128 + 16 = 1010.

### Biến thể
- **F&B**: segmented `Mang về / Tại chỗ / Ship` quan trọng; add-on row dùng Topping nhiều. `Phòng bàn` mở màn sơ đồ bàn [suy ra: lưới thẻ bàn 4–6 cột trong card, trạng thái Trống / Đang phục vụ / Đã đặt dùng Tag Gray / Blue / Amber].
- **Khách sạn** [suy ra]: như F&B, đổi `Phòng bàn` thành sơ đồ phòng; dòng giỏ hàng có thêm ngày nhận/trả phòng ở dòng thuộc tính.
- **Chế độ bán** trên top bar (`Bán thường ▾`) giữ nguyên ở mọi biến thể.

### Trạng thái cần có
`Mặc định` (có 3–4 dòng hàng, 1 dòng có quà tặng + topping) · `Giỏ trống` · `Thanh toán` (popup Payment modal) · `Toast` (sau khi lưu hoặc thanh toán).

---

## 2. Trang quản lý — danh sách [suy ra]

Cho các màn như Danh sách phiếu kiểm kê, Sản phẩm, Khách hàng, Đơn hàng. Bản gốc chưa có spec; mẫu này dựng từ cùng khung POS, **cần designer xác nhận** trong lần vẽ đầu.

```
  70 │ TOP BAR (quản lý)                                               │
     ├────┬─────────────────────────────────────────────────────────────┤
     │RAIL│ padding 16 · gap 16                                         │
     │ 72 │ PAGE HEADER: tiêu đề ··················· [Phụ] [+ Chính] 48 │
     │    │ ┌ CARD bảng (co giãn, radius 16) ─────────────────────────┐ │
     │    │ │ FILTER BAR                                           72 │ │
     │    │ │ DATA TABLE header 48 + dòng 56                          │ │
     │    │ │ PAGER                                                48 │ │
     │    │ └─────────────────────────────────────────────────────────┘ │
```

- **Top bar quản lý**: cao 70, `blue/500`; Brand → (khoảng trống) → nút `Bán hàng` (nút trắng như Chế độ bán, icon `ShoppingCart`, quay về POS) → `Bell` 40×40 kèm Count badge Red → Tài khoản → Menu. Không có ô tìm kiếm hàng hóa và tab hóa đơn.
- **Rail**: như POS, mục active theo phân hệ (Kho cho kiểm kê kho, Sản phẩm, Khách hàng…).
- **Card bảng**: rộng 1816, cao = 1010 − 16 − 48 − 16 − 16 = 914.
- Số dòng mẫu: 10–12 dòng, có đủ các trạng thái của cột Trạng thái.
- Trạng thái cần có: `Mặc định` · `Trống` · `Đang lọc` (nếu wireframe có bộ lọc đáng chú ý).

## 3. Trang quản lý — chi tiết / biểu mẫu nhiều bước [suy ra]

Cho màn tạo/sửa phiếu, ví dụ Kiểm kê Bước 1, Bước 2.

- Top bar quản lý + rail như §2.
- Main dọc, padding 16, gap 16: Page header (nút `ChevronLeft` 40×40 quay lại + tiêu đề + Stepper các bước căn phải nếu có nhiều bước) → Form section (các trường chung: kho, ngày, phạm vi…) → Card bảng (danh sách dòng, cho phép nhập trong bảng) → Sticky footer 72 (ghim ở đáy frame).
- Trường bị khóa (wireframe ghi `(khóa)`) → Input Disabled, giữ giá trị.
- Trạng thái cần có: `Mặc định` · `Lỗi validate` (ít nhất một trường lỗi kèm thông báo nguyên văn) · các popup mà luồng dẫn tới.

## 4. Popup trên màn

Frame 1920×1080 = bản sao màn nền + scrim `overlay/scrim` phủ toàn màn + Modal căn giữa. Chọn rộng: 480 (xác nhận, form ngắn), 640 (form 2 cột hoặc bảng ít cột), 800 (bảng như chọn lô). Bảng trong popup dùng Data table, tối đa 6 dòng mẫu, phần thân cuộn.

## 5. Trang thông báo / trạng thái toàn trang

Card trắng giữa màn, rộng 640, padding 40, căn giữa: minh họa 3D (vùng 200×200, để placeholder nếu chưa có ảnh) → tiêu đề (được viết IN HOA nếu là thông báo ngắn, vd `NÂNG CẤP VÀ BẢO TRÌ HỆ THỐNG`, `Display/H5`) → mô tả `Body/lg` `text/secondary`, xưng "Quý khách" → nút Primary (nếu có) → `Hotline 1900 3369` `Body/md`.
