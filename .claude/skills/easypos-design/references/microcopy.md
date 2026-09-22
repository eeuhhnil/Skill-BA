# Nội dung và câu chữ

## Ngôn ngữ
- Tiếng Việt, **luôn đủ dấu**. Không viết không dấu, không viết tắt làm mất dấu.
- Tiếng Anh chỉ có ở tên tính năng đã quen trong sản phẩm: `QR order`, `Demopro`, `Combo`, `Topping`, `Ship`, `of 100`.
- Giữ **nguyên văn chữ trên wireframe** (đã được chốt). Chỉ sửa lỗi chính tả rõ ràng và ghi vào log.

## Giọng văn
- Thực tế, ngắn, hướng hành động — người dùng là nhân viên bán hàng đang bận.
- Nhãn là cụm danh từ hoặc động từ mệnh lệnh ngắn, không phải câu: `Bán hàng`, `Thanh toán`, `Lưu đơn`, `Chọn lô`, `Ghi chú`, `Thực đơn`, `Phòng bàn`, `Cân bằng kho`.
- Trong app: câu mệnh lệnh trung tính, **không** dùng "tôi/bạn".
- Thông báo toàn trang gửi chủ cửa hàng: xưng **"Quý khách"**, vd *"Mong Quý khách thông cảm vì sự bất tiện này!"*.
- Thông báo lỗi nói rõ sai gì và làm gì tiếp, vd `Vui lòng chọn kho hàng`, `Số lượng thực tế không được âm`.

## Viết hoa
- **Viết hoa kiểu câu** cho nút, nhãn, menu, tiêu đề cột: `Tổng tiền hàng`, không phải `Tổng Tiền Hàng`.
- IN HOA chỉ cho tiêu đề ngắn của thông báo toàn trang. Không in hoa nút và nội dung.
- Tên riêng giữ đúng cách viết: `EasyPOS`, `SoftDreams`, `Công ty Cổ phần SDS`.

## Số, tiền, ngày
- Tiền: dấu chấm phân cách hàng nghìn, `đ` viết liền phía sau: `5.000.000đ`, `30.000đ`. Trong cột bảng có thể bỏ `đ`: `35.000`.
- Số lượng: `1.000 điểm`, `125`. Số thập phân dùng dấu phẩy: `1,5 kg`.
- Ngày `DD/MM/YYYY`: `16/09/2024`. Khoảng ngày: `01/09/2024 – 22/09/2024`. Giờ `HH:mm`: `14:30 16/09/2024`.
- Mã chứng từ: `HĐ 001`, `KK000123` (theo tiền tố của nghiệp vụ nếu wireframe có).
- Số trong bảng: font số, đậm, căn phải; tổng tiền in đậm màu xanh.

## Emoji
Không dùng emoji trong UI. Emoji trên wireframe chỉ là ký hiệu thay icon, chuyển sang icon theo `excalidraw-mapping.md`.

## Dữ liệu mẫu
Dùng khi wireframe chỉ có tiêu đề cột. Chọn theo ngành của màn:

**Bán lẻ (thời trang/điện máy)**
| Tên | ĐVT | Giá | Giá cũ | Tồn | Khuyến mãi |
|---|---|---|---|---|---|
| Iphone 17 Promax | Chiếc | 30.000 | 35.000 | 125 | Mua 2 tặng 1 |
| Áo thun OWL trắng | Chiếc | 199.000 | 250.000 | 84 | Mua 2 tặng 1 |
| Quần jean nam slim | Chiếc | 459.000 | — | 42 | — |
| Áo sơ mi Oxford | Chiếc | 329.000 | 380.000 | 60 | — |
| Khăn quàng cổ nữ OWL | Chiếc | 89.000 | — | 210 | Quà tặng |
| Mũ lưỡi trai basic | Chiếc | 120.000 | 150.000 | 95 | — |
| Giày sneaker trắng | Đôi | 690.000 | 790.000 | 33 | Mua 2 tặng 1 |
| Túi tote canvas | Chiếc | 149.000 | — | 120 | — |
| Áo khoác gió 2 lớp | Chiếc | 549.000 | 620.000 | 8 (Sắp hết) | — |
| Thắt lưng da nam | Chiếc | 259.000 | — | 0 (Hết hàng) | — |
| Vớ cotton (combo 5) | Bộ | 99.000 | 130.000 | 300 | Mua 2 tặng 1 |
| Kính mát thời trang | Chiếc | 219.000 | — | 65 | — |

Danh mục: `Tất cả` · `Quần áo` · `Áo` · `Quần` · `Áo sơ mi` · `Khăn` · `Mũ` · `Giày`.

**Kho**: `Kho chính`, `Kho mặc định`, `Kho chi nhánh Cầu Giấy`. Lô: `LO2:05/05/2025`, NSX `05/05/2025`, HSD `05/05/2026`.

**Khách hàng**: `Khách lẻ`, `Nguyễn Văn An – 0912 345 678`, `Công ty TNHH Minh Phát`.

**Người dùng / cửa hàng**: `Công ty Cổ phần SDS`, nhân viên `Trần Thu Hà`.

## Bảng câu chữ dùng nguyên văn

| Ngữ cảnh | Câu chữ |
|---|---|
| Tìm kiếm | `Tìm kiếm hàng hóa` |
| Barcode | `Tìm kiếm barcode` |
| Bảng giá | `Bảng giá chung` |
| Khách hàng | `Khách lẻ` · `1.000 điểm` · `Ví: 125.000đ` |
| Tab hóa đơn | `HĐ 001` |
| Chế độ bán | `Bán thường` |
| Hình thức | `Mang về` · `Tại chỗ` · `Ship` |
| Nút header | `Thực đơn` · `Phòng bàn` |
| Cột giỏ hàng | `Tên sản phẩm` · `SL` · `Đơn giá` · `Giảm giá` · `Thuế` · `Thành tiền` |
| Dòng hàng | `Chiếc · Kho mặc định · Demopro` · `LO2:05/05/2025` · `Chọn lô` · `Ghi chú` |
| Tag phụ | `Quà tặng` · `Topping` |
| Khuyến mãi | `Mua 2 tặng 1` |
| Tổng | `Tổng tiền hàng (4)` → `5.000.000đ` |
| Ngày tạo | `Ngày tạo: 16/09/2024` |
| Hành động | `Lưu đơn` (F8) · `Thanh toán` (F9) |
| Tab picker | `Sản phẩm` · `Combo` · `Dịch vụ` |
| Phân trang | `1-16 of 100` · `50 bản ghi/trang` |
| Popup thanh toán | `Thanh toán` · `Khách cần trả` · `Tiền mặt` / `Thẻ` / `Chuyển khoản` · `Tiền khách đưa` · `Tiền thừa trả khách` · `Hoàn thành` |
| Giỏ trống | `Chưa có hàng hóa trong đơn` / `Chọn sản phẩm ở danh sách bên phải để thêm vào đơn` |
| Picker trống | `Chưa có combo nào` / `Chưa có dịch vụ nào` |
| Bảng trống | `Chưa có dữ liệu` |
| Toast thành công | `Đã lưu đơn vào danh sách đơn lưu` · `Thanh toán thành công · Đã in hóa đơn` |
| Toast cảnh báo | `Đơn hàng đang trống` |
| Tồn kho | `Còn hàng` · `Sắp hết` · `Hết hàng` |
| Trạng thái đơn | `Hoàn thành` · `Hủy` |
| Nút chung | `Lưu` · `Hủy` · `Quay lại` · `Tiếp tục` · `Đồng ý` · `Xóa` · `In` · `Xuất file` · `Xóa lọc` |
| Hỗ trợ | `Hotline 1900 3369` |
