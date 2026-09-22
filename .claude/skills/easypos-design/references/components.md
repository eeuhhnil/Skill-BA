# Components EasyPOS

Mỗi mục: kích thước · padding/gap · radius · màu · chữ · icon · trạng thái · **thuộc tính Figma** (variant / boolean / instance swap / text). Tên màu, chữ, radius là tên trong `tokens.md`. Mục có nhãn **[suy ra]** không có trong bản gốc, được dựng theo quy tắc chung — cần designer xác nhận.

Trạng thái chung cho mọi thành phần tương tác:
- **Hover** → nền đậm hơn một bậc (`action/primary-hover`), hoặc nền tint với thành phần phụ.
- **Pressed** → `action/primary-pressed`, dịch xuống 1px.
- **Focus** → viền `blue/500` + `Focus/ring`.
- **Disabled** → nền `surface/disabled`, chữ `text/placeholder`.

---

## 1. Cơ bản

### Button
| Hierarchy | Nền | Chữ | Viền |
|---|---|---|---|
| Primary | `action/primary` | `text/on-primary` | — |
| Secondary | `surface/default` | `blue/500` | 1.2px `blue/500` |
| Tertiary | `action/tint` | `blue/500` | — |
| Ghost | trong suốt | `blue/500` | — |
| Destructive | `action/destructive` | `text/on-primary` | — |

| Size | Chữ | Padding | Cao | Radius |
|---|---|---|---|---|
| L | `Button/lg` | 8 × 24 | 40 | `radius/md` |
| M | `Button/md` | 6 × 16 | 32 | `radius/md` |
| S | `Button/sm` | 4 × 12 | 26 | `radius/sm` |

Icon 20 (L), 18 (M), 16 (S), cách chữ 8. **Figma:** `Hierarchy` (Primary/Secondary/Tertiary/Ghost/Destructive) · `Size` (L/M/S) · `State` (Default/Hover/Pressed/Focus/Disabled) · boolean `Leading icon`, `Shortcut` · instance swap `Icon` · text `Label`, `Key`.

### Keycap (phím tắt trong nút)
Padding 2 × 8, radius `radius/xs`, chữ 15/700. Trên nút Primary: nền `overlay/keycap-on-primary`, chữ trắng. Trên nút Secondary/Tertiary: nền `blue/200`, chữ `blue/700`. **Figma:** `On` (Primary/Secondary).

### Input
Cao 40, padding 0 × 12, radius `radius/sm`, viền 1px `border/default`, nền trắng, chữ `Body/lg` `text/primary`, placeholder `text/placeholder`. Icon đầu 20 màu `text/secondary`, cách chữ 8.
- Focus: viền `blue/500` + `Focus/ring`, icon chuyển `blue/500`.
- Error: viền `error/500`, icon `AlertCircle` `error/500` ở cuối, dòng lỗi `Body/sm` `error/700` dưới ô, cách 4.
- Disabled/read-only: nền `surface/disabled`, chữ `text/tertiary`.
Nhãn phía trên: `Label` `text/secondary`, cách ô 8; trường bắt buộc thêm ` *` màu `error/500`.
**Figma:** `State` (Default/Focus/Filled/Error/Disabled) · boolean `Label`, `Leading icon`, `Required`, `Helper` · text `Label`, `Value`, `Helper`.

### Select / Dropdown
Như Input, thêm `ChevronDown` 18 `text/secondary` ở cuối. Menu mở: nền trắng, radius `radius/lg`, `Shadow/md`, padding 4; mỗi dòng cao 40, padding 0 × 12, hover `blue/50`, dòng đang chọn chữ `blue/500` + `Check` 18 ở cuối.

### Date picker [suy ra]
Input có icon `Calendar` 18 ở cuối, giá trị `DD/MM/YYYY`. Khoảng ngày: `01/09/2024 – 22/09/2024`.

### Search field
Như Input có icon `Search`; placeholder `Tìm kiếm hàng hóa` (hoặc theo wireframe). Trên top bar: nền trắng, không viền, radius `radius/md`, rộng 360.

### Checkbox · Radio · Toggle
- **Checkbox** 20×20, radius 6, viền 1.5px `border/strong`. Bật: nền `blue/500`, icon `Check` 14 trắng. Nửa chọn: nền `blue/500`, icon `Minus` 14.
- **Radio** 20×20 tròn, viền 1.5px `border/strong`. Bật: viền `blue/500` + chấm 10px `blue/500`.
- **Toggle** 40×22, radius full, nền `gray/100` (tắt) / `blue/500` (bật), núm 18px trắng cách mép 2.
**Figma:** `Checked` (Off/On/Mixed) · `State` (Default/Hover/Disabled) · text `Label` (nhãn đặt bên phải, cách 8, `Body/md`).

### Tag
Chữ 12/600, padding 2 × 8, radius `radius/sm`.
| Tone | Nền | Chữ | Ví dụ |
|---|---|---|---|
| Green | `success/50` | `success/700` | Quà tặng, Hoàn thành, Mua 2 tặng 1, Đã xử lý |
| Orange | `orange/50` | `orange/700` | Topping |
| Blue | `blue/100` | `blue/700` | Demopro, nhãn |
| Amber | `warning/50` | `warning/700` | Sắp hết, Chưa xử lý |
| Red | `error/50` | `error/700` | Hủy, lỗi |
| Gray [suy ra] | `surface/subtle` | `text/secondary` | Nháp, không hoạt động |
**Figma:** `Tone` · text `Label`.

### Status dot
Chấm 8px + chữ `Body/sm` `text/secondary`, cách 6. `Còn hàng` `success/500` · `Sắp hết` `warning/500` · `Hết hàng` `error/500`. **Figma:** `Status`.

### Count badge
Cao 20, min-width 20, padding 0 × 6, radius full, chữ 12/700 trắng. Nền `error/500` mặc định; trên top bar dùng `orange/500`. **Figma:** `Tone` (Red/Orange) · text `Count`.

### Chip lọc (category)
Cao 32, padding 0 × 12, radius `radius/sm`, viền 1px `border/default`, nền trắng, chữ `Label` `text/secondary`; số đếm `(125)` chữ 400 `text/placeholder`. Active: nền `blue/100`, viền `blue/200`, chữ `blue/700`, số đếm `blue/500`. **Figma:** `State` (Default/Hover/Active) · text `Label`, `Count` · boolean `Count`.

### Segmented control
Vỏ: nền `surface/subtle`, radius `radius/md`, padding 4, gap 4, cao 48. Nút: cao 40, padding 0 × 16, radius `radius/sm`, chữ 15/500 `text/secondary`, icon 18 cách chữ 8. Active: nền trắng, chữ `blue/500` 600, `Shadow/sm`. **Figma:** vỏ chứa 2–4 instance `Segment` (`Active` true/false).

### Tabs
Chữ 16/600 `text/secondary`, padding dưới 12, gap giữa tab 24, đường kẻ dưới 1px `border/faint`. Active: chữ `blue/500` + gạch dưới 3px `blue/500` bo góc trên 3. **Figma:** `Tab` (`Active`).

### Pager
Chữ `Number/sm`: `1-16` `text/primary` + ` of 100` `text/secondary`. Nút 32×32, radius `radius/sm`, viền `border/default`, icon `ChevronLeft/Right` 16. Active/khả dụng: nền `blue/500`, icon trắng. Kèm tùy chọn `50 bản ghi/trang` (Select size S) ở bên trái [suy ra từ wireframe kiểm kê].

### Quantity stepper
Nút 24×24, radius `radius/sm`, nền `blue/500`, icon `Minus`/`Plus` 14 trắng; số ở giữa `Number/table`, min-width 16, gap 8. SL = 1 thì nút trừ disabled.

### Avatar
Tròn, 38 (top bar, viền 2px `white @50%`) hoặc 40 (khách hàng). Không có ảnh: nền `blue/100`, chữ cái đầu `Title/md` `blue/700`.

### Tooltip [suy ra]
Nền `ink`, chữ `Body/sm` trắng, padding 4 × 8, radius `radius/sm`. Dùng cho icon không có nhãn (mục rail).

---

## 2. Khung POS

### Top bar
Cao 70, nền `blue/500`, padding 0 × 20, gap 16, căn giữa theo chiều dọc. Thứ tự: Brand → Search (360) → Tab hóa đơn + nút thêm → QR order → (khoảng trống) → Chế độ bán → Tài khoản → Menu.
- **Brand**: mark 32×32 trắng + wordmark `Brand/Wordmark` trắng, cách 8. Logo là bản dựng lại; thay bằng SVG chính thức khi có.
- **Nút top bar** (tab `HĐ 001`, `+`, `QR order`, menu): cao 40, radius `radius/md`, nền `overlay/on-primary`, chữ 15/600 trắng, icon 18–20, padding 0 × 16 (nút chỉ có icon: 40×40). QR order kèm Count badge Orange.
- **Chế độ bán** (`Bán thường ▾`): cao 48, radius `radius/md`, nền trắng, chữ 16 `blue/500`, phần tên in đậm 700, icon `ShoppingCart` + `ChevronDown` 20.
- **Tài khoản**: Avatar 38 + tên `Công ty Cổ phần SDS` 15/600 trắng, cách 12.

### Left rail
Rộng 72, nền trắng, viền phải 1px `border/default`, padding 16 × 0, gap 8, mục căn giữa. Mục 48×48, radius `radius/md`, icon 24 `icon/muted`. Hover: nền `blue/50`, icon `blue/400`. Active: nền `blue/100`, icon `blue/500`. Có Tooltip với tên mục.

12 mục theo thứ tự: `Bán hàng` LayoutGrid · `Đơn hàng` ShoppingCart · `Sản phẩm` Package · `Đơn lưu` Bookmark · `Khuyến mãi` TicketPercent · `Khách hàng` Users · `Kho` Layers · `Giao dịch` ArrowLeftRight · `Báo cáo` ChartColumn · `Sổ quỹ` CreditCard · `Trang chủ` Home · `Cài đặt` Settings.

### Order header
Cao 48, gap 16. Thứ tự: Khách hàng → Segmented (`Mang về` ShoppingBag · `Tại chỗ` Utensils · `Ship` Truck) → Bảng giá → (khoảng trống) → `Thực đơn` (Button L Primary, icon List) → `Phòng bàn` (Button L Secondary kiểu viền xám, icon Grid2x2).
- **Khách hàng**: Avatar 40 + tên `Title/md` + dòng meta `Body/sm` `text/secondary` gap 12: `Star` 14 `warning/500` `1.000 điểm` · `Wallet` 14 `blue/400` `Ví: 125.000đ`.
- **Bảng giá** (`Bảng giá chung ▾`): cao 48, viền `border/default`, radius `radius/md`, chữ 15/500, icon `MapPin` 18 `blue/500` + `ChevronDown` 18.
- Nút trên header cao 48 (ngoại lệ so với Button L).

### Cart table
Card trắng radius `radius/xl`. Header: padding 16 × 20, chữ 14/500 `text/secondary`, kẻ dưới 1px `border/faint`. Cột: `Tên sản phẩm` (co giãn) · `SL` 92 giữa · `Đơn giá` 112 phải · `Giảm giá` 100 phải · `Thuế` 80 phải · `Thành tiền` 128 phải · 40 (xóa).

**Cart row**: padding 16 × 20 × 8, căn trên.
- Thumbnail 56×56, radius `radius/md`, nền `surface/subtle`, cách tên 16.
- Tên `Title/md` + icon `Copy` 16 `blue/400` cách 8.
- Dòng thuộc tính `Body/sm` `text/secondary`: `Chiếc · Kho mặc định · Demopro`.
- Dòng lô: `ShieldCheck` 14 `blue/400` `12 tháng` · `LO2:05/05/2025` · `X` 14 `text/placeholder` · link `Chọn lô` 13/500 `blue/500`, gap 8.
- Link `Paperclip` 14 `Ghi chú` `Body/sm` `text/secondary`.
- Số `Number/table` căn phải; Đơn giá có gạch chân chấm `border/strong` (bấm để sửa); Thành tiền màu `blue/500`.
- Nút xóa `Trash2` 18 `icon/muted`, hover `error/500`.

**Add-on row** (quà tặng/topping, dưới dòng hàng): padding trái 92, cao 28, gap 8, chữ `Body/md` `text/secondary`. Icon 18 `icon/muted`: `Gift` cho quà tặng, `CirclePlus` cho topping. Tag Green `Quà tặng` / Orange `Topping` · tên · SL `Number/table`.

**Cart empty**: giữa card, icon `ShoppingCart` 56 `icon/empty`, tiêu đề 18/600 `Chưa có hàng hóa trong đơn`, mô tả `Body/md` `text/secondary` `Chọn sản phẩm ở danh sách bên phải để thêm vào đơn`, gap 8.

### Product picker
Card trắng radius `radius/xl`.
- Tabs `Sản phẩm · Combo · Dịch vụ`, padding 16 × 20 × 0; nút danh sách 32×32 `surface/subtle` radius `radius/md` ở cuối.
- Hàng tìm kiếm padding 12 × 20, gap 12: Search field (co giãn) · `Tìm kiếm barcode` + Toggle (bật) · nút lọc 40×40 viền `border/default` radius `radius/md` icon `SlidersHorizontal` 20 `blue/500`.
- Chip lọc: padding 4 × 20 × 12, gap 8, cuộn ngang.
- Lưới 2 cột, gap 12, padding 4 × 20 × 12, cuộn dọc.
- Pager ở đáy, padding 8 × 20, kẻ trên 1px `border/faint`, căn phải.
- Tab trống: icon `Package2` / `ConciergeBell` 48 `icon/empty` + `Chưa có combo nào` / `Chưa có dịch vụ nào`.

**Product card**: padding 12, gap 12, viền 1px `border/faint`, radius `radius/lg`, nền trắng. Hover: viền `blue/200` + `Shadow/md`.
- Thumbnail 64×64 radius `radius/md` `surface/subtle`.
- Tên 15/600 + ` - Chiếc` 400 `text/secondary`, tối đa 2 dòng.
- Meta gap 8: Status dot theo tồn kho + số tồn `Number/sm` · Tag Green khuyến mãi nếu có.
- Giá: giá cũ gạch ngang 13 `text/placeholder` · giá bán `Number/body` `blue/500` + `đ`.
**Figma:** boolean `Old price`, `Promo` · `Stock` (Còn hàng/Sắp hết/Hết hàng) · `State` (Default/Hover).

### Bottom bar
Cao 128, gap 16, hai phần cùng tỉ lệ với vùng làm việc (trái = rộng cart, phải = rộng picker).
- **Trái** (dọc, gap 16):
  - Ô tổng: cao 64, nền trắng, viền `border/default`, radius `radius/md`, padding 0 × 20. Trái `Tổng tiền hàng (4)` 16 `text/secondary`; phải `5.000.000đ` `Number/lg` `blue/500` + `CircleChevronRight` 24 `blue/500`, gap 12.
  - Hàng meta (gap 16): `Calendar` 18 + `Ngày tạo: ` + **`16/09/2024`** 15 `text/secondary` · ô ghi chú cao 48 (Input có icon `Paperclip`, placeholder `Ghi chú`, radius `radius/md`).
- **Phải** (ngang, gap 16), nút cao hết 128, radius `radius/md`, chữ `Button/action`, keycap cách chữ 12:
  - `Lưu đơn` + keycap `F8`: rộng 46%, nền `action/tint`, viền 1px `blue/500`, chữ `blue/500`; hover `action/tint-hover`.
  - `Thanh toán` + keycap `F9`: co giãn, nền `action/primary`, chữ trắng; hover `action/primary-hover`.

---

## 3. Lớp phủ

### Modal
Rộng 480 (form nhỏ) hoặc 640/800 (bảng trong popup) [640/800 suy ra], nền trắng, radius `radius/xl`, `Shadow/lg`, padding 24, trên scrim `overlay/scrim` phủ toàn màn. Header: tiêu đề `Display/Modal title` + nút đóng 32×32 `surface/subtle` radius `radius/md` icon `X` 18, cách nội dung 16. Footer [suy ra cho modal có 2 nút]: căn phải, gap 12, Button L Secondary (`Hủy`/`Quay lại`) + Primary (hành động chính); popup chỉ một hành động thì dùng nút xác nhận toàn chiều rộng cao 56.

### Payment modal (480)
- Hộp số tiền: nền `blue/50`, radius `radius/md`, padding 16 × 20; `Khách cần trả` 16 `text/secondary` · số `Number/xl` `blue/500`. Cách dưới 16.
- Phương thức (3 ô, gap 12): padding 12 × 0, viền `border/default`, radius `radius/md`, icon 24 trên chữ 14/500, gap 8. Active: viền `blue/500`, nền `blue/50`, chữ `blue/500` 600. `Tiền mặt` Banknote · `Thẻ` CreditCard · `Chuyển khoản` QrCode.
- `Tiền khách đưa`: nhãn `Label`, ô cao 48 radius `radius/md`, số `Number/md` căn phải + `đ` 18 `text/secondary`.
- Nút số nhanh (4 nút, gap 8): cao 36, nền `surface/subtle`, radius `radius/md`, chữ 14/600 số; hover `blue/100` chữ `blue/600`.
- `Tiền thừa trả khách` 16 `text/secondary` · số `Number/md` `success/500`.
- Nút `Hoàn thành`: toàn chiều rộng, cao 56, nền `blue/500`, radius `radius/md`, chữ 18/700 trắng, icon `CircleCheckBig` 24.

### Toast
Đặt giữa, cách đáy 32. Padding 12 × 24, radius `radius/md`, `Shadow/lg`, chữ 16/600, icon 24, gap 12.
- Thành công: nền `success/500`, chữ và icon trắng, icon `CircleCheckBig`.
- Cảnh báo: nền `warning/500`, chữ và icon `ink`, icon `TriangleAlert`.
- Lỗi [suy ra]: nền `error/500`, chữ và icon trắng, icon `AlertCircle`.

### Confirm dialog [suy ra]
Modal 480: icon tròn 48 (nền `warning/50` + `TriangleAlert` 24 `warning/500`, hoặc `error/50` + `error/500` với thao tác xóa), tiêu đề `Title/lg`, mô tả `Body/md` `text/secondary`, footer 2 nút. Hành động xóa/hủy dùng Button Destructive.

---

## 4. Thành phần cho trang quản lý [suy ra]

Dùng cho các màn ngoài Bán hàng (danh sách phiếu, sản phẩm, khách hàng…), xem `layouts.md` §2.

### Page header
Cao 48: tiêu đề `Display/H5` `text/primary` bên trái; bên phải các nút Button L (hành động chính là Primary có icon `Plus`, vd `+ Kiểm kê kho`; hành động phụ Secondary như `Xuất file`).

### Filter bar
Hàng ngang gap 12, căn trái: Search field rộng 320 + Select/Date picker rộng 200–240 + Ghost `Xóa lọc`. Nằm trong card bảng, padding 16 × 20, kẻ dưới `border/faint`.

### Data table
Trong card trắng radius `radius/xl`.
- Header: cao 48, padding 0 × 20, chữ 14/500 `text/secondary`, nền `surface/subtle`, kẻ dưới `border/faint`.
- Dòng: cao 56, padding 0 × 20, chữ `Body/md` `text/primary`, kẻ dưới `border/faint`; hover nền `blue/50`; dòng đang chọn nền `blue/100`.
- Cột mã: chữ `blue/500` 500 (link mở chi tiết). Cột số `Number/table` căn phải. Cột trạng thái dùng Tag. Cột thao tác 40–96 chứa icon button 32×32 (`SquarePen`, `Trash2`, `Printer`, `Eye`) màu `icon/muted`, hover `blue/500` (xóa: `error/500`).
- Cột chọn: Checkbox, rộng 48. Khi có dòng được chọn: thanh `Đã chọn 2 sản phẩm` nền `blue/50` thay cho filter bar, kèm hành động hàng loạt.
- Ô nhập trong bảng (vd `Tồn TT`): Input cao 32, số căn phải.
- Trống: icon 48 `icon/empty` + `Chưa có dữ liệu` + (nếu hợp) nút Primary tạo mới.
- Pager ở đáy card.

### Stepper các bước
Hàng ngang: vòng tròn 28 (xong: nền `blue/500` + `Check` trắng; đang làm: viền 2px `blue/500` + số `blue/500`; chưa tới: viền `border/strong` + số `text/placeholder`) + nhãn `Title/sm`, nối nhau bằng đường 1px `border/strong` (đoạn đã qua `blue/500`).

### Form section
Card trắng radius `radius/xl`, padding 20; tiêu đề `Title/lg`, cách nội dung 16; trường xếp lưới 2–3 cột gap 16 × 24.

### Sticky footer
Cao 72, nền trắng, kẻ trên `border/default`, padding 0 × 24, nút căn phải gap 12: Secondary (`Quay lại`, `Lưu tạm`) + Primary (`Tiếp tục`, `Cân bằng kho`).
