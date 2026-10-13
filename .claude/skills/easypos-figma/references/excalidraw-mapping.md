# Đọc wireframe Excalidraw và chuyển sang component

## 1. Đọc file

```
PYTHONUTF8=1 python .claude/skills/easypos-figma/scripts/read_excalidraw.py <file.excalidraw>          # bản đọc cho người
PYTHONUTF8=1 python .claude/skills/easypos-figma/scripts/read_excalidraw.py <file.excalidraw> --json   # khi cần tọa độ để dựng
```

Thiếu `PYTHONUTF8=1` thì tiếng Việt bị vỡ trên Windows.

Kết quả gồm:
- **Màn**: mỗi hình chữ nhật lớn (≥ 300×150) không nằm trong hình khác. Tiêu đề lấy từ dòng chữ có số thứ tự ①②③ (hoặc `1`, `3a`) ngay phía trên khung.
- **Phần tử** trong mỗi màn, tọa độ tính từ góc trái trên của màn, xếp theo dòng. `control` = ô nhỏ chứa đúng một dòng chữ (nút, ô nhập, select).
- **Luồng**: mũi tên từ màn nào sang màn nào, kèm nhãn. Mũi tên không gắn vào khung thì script đoán theo điểm đầu/cuối gần màn nào nhất, nên **kiểm lại bằng mắt** khi luồng trông vô lý.
- **Ghi chú**: chữ cam, gắn với màn gần nhất.

Script không đoán được ý nghĩa, chỉ gom dữ liệu. Việc hiểu phần tử là gì theo các quy tắc dưới đây.

## 2. Quy ước màu trên wireframe của team

| Màu Excalidraw | Nghĩa | Xử lý |
|---|---|---|
| `#1e1e1e` viền/chữ đen | cấu trúc và chữ UI chính | vẽ |
| `#868e96` chữ xám | nhãn, placeholder, chữ UI phụ | vẽ; xét ngữ cảnh để biết là placeholder hay nhãn |
| `#ced4da` viền xám nhạt | kẻ dòng bảng | Data table row |
| `#f1f3f5` nền | thanh tiêu đề màn/popup | Page header, hoặc header của Modal |
| `#dee2e6` nền (nút) | nút chính | Button Primary |
| `#1971c2` chữ xanh | nhãn luồng trên mũi tên | **không vẽ** thành chữ; là hành động kích hoạt ở màn nguồn |
| `#e67700` chữ cam / `#fff3bf` nền vàng | ghi chú, điểm chưa chốt (`BRIEF KHÁC: …`) | **không vẽ**; đưa vào Discovery để hỏi |

Đầu dòng tiêu đề màn: `①` màn chính, `③a` màn con hoặc popup của ③. Chữ `(…)` sau tiêu đề là chú thích cho người đọc, không phải nội dung UI.

## 3. Nhận dạng phần tử

Cột "Loại phần tử" là loại chung; tên component thật tra trong `design-kit.md` của kit đã chọn. Cột "Kit `pos`" ghi sẵn tên component set trong kit EasyPOS. Kit không có loại đó → dựng theo màn tham chiếu cùng loại trong file đích (clone), hoặc ghép từ atom và ghi "phần tự ghép".

| Trên wireframe | Loại phần tử | Kit `pos` | Ghi chú |
|---|---|---|---|
| Ô có nền `#dee2e6` + chữ động từ | Nút chính | `Button` · Hierarchy=Primary | Mỗi vùng chỉ có một nút Primary |
| Ô viền, không nền + chữ động từ | Nút phụ | `Button` · Hierarchy=Secondary | `Hủy`, `Quay lại`, `Nhập Excel`… |
| Chữ bắt đầu bằng `+` | Nút có icon thêm | `Button` + icon `add` | Bỏ dấu `+` khỏi nhãn |
| Ô dài có chữ xám | Ô nhập, chữ xám = placeholder | `Component 1` (Input text field) | Có `🔍` → ô tìm kiếm |
| Chữ + `▾` trong ô | Dropdown | `Input Dropdown` | `Lọc ▾` → `Filter Dropdown` |
| Chữ + `📅` hoặc dạng ngày trong ô | Chọn ngày | `Date Picker` (Date / Date range) | `01/09 – 22/09` → khoảng ngày, viết đủ năm |
| Nhãn có ` *` phía trên ô | Ô nhập bắt buộc | lớp `Red dot` của Input | |
| `(khóa)` sau giá trị | Ô nhập disabled / read-only | | Bỏ chữ `(khóa)`, giữ giá trị |
| `Kho: Kho chính` (nhãn: giá trị, không có ô) | Cặp nhãn–giá trị chỉ đọc | text style | |
| `○ … ● …` | Radio group | `Checkbox-Base` · Type=Radio | `●` = đang chọn |
| `☐` / `☑` | Checkbox Off / On | `Checkbox-Base` | Ở cột đầu bảng → cột chọn |
| `[Tất cả 3] [Chưa kiểm 1] …` | Tab / chip lọc có số đếm | `Tab Navigation (Horizontal)`, `Chips` | Phần tử đầu = đang chọn |
| `(1) Bước A ───── (2) Bước B`, `✓` = xong | Stepper các bước | không có trong kit → màn tham chiếu | |
| Hàng ô liền nhau + kẻ `#ced4da` | Bảng dữ liệu | không có set → màn tham chiếu | Hàng đầu = header; dòng đầu có chữ thường là dữ liệu mẫu |
| Ô nhỏ trong dòng bảng | Ô nhập trong bảng | Input | Cột số → căn phải |
| `↳ [Chọn lô] (hàng có lô)` | Dòng con + link | | |
| `Chưa xử lý`, `Đã xử lý`… trong cột trạng thái | Nhãn trạng thái | `Badge` | Chưa xử lý = Warning, Đã xử lý/Hoàn thành = Success, Hủy = Error, Nháp = Gray |
| `‹ 1 2 3 ›`, `50 bản ghi/trang` | Phân trang | `Pagination` | |
| Ô lớn, trống, dưới nhãn `Ghi chú…` | Ô nhập nhiều dòng | `Text area` | |
| Khung nhỏ hơn màn, có thanh tiêu đề | Popup trên màn nguồn | không có set → màn tham chiếu | Nền scrim dùng `figma.overlay` |
| Thông báo nổi sau hành động | Toast | `Toast Bar` | |
| Dòng chữ xám dài giải thích quy tắc | **Chú thích cho người đọc**, không vẽ | | Đưa vào log để chuyển sang SRS |

Không chắc một dòng chữ là UI hay chú thích → không vẽ, ghi vào câu hỏi mở.

## 4. Emoji → icon

Tên icon theo bộ Iconsax của kit `pos` (mục "Icons" trong `design-kit.md`, lấy biến thể `Property 1=linear`). Kit khác thì tra tên tương ứng trong kit đó.

| Emoji | Iconsax | | Emoji | Iconsax |
|---|---|---|---|---|
| 🔍 | `search-normal` | | ✎ ✏️ | `edit-2` |
| 🗑 | `trash` | | 🖨 | `printer` |
| 📅 | `calendar` | | ☰ | `menu` |
| ▾ | `arrow-down` | | ‹ › | `arrow-left` / `arrow-right` |
| ✕ ✖ | `close-circle` | | ✓ ✔ | `tick-circle` |
| ⚙ | `setting-2` | | 👁 | `eye` |
| ⬇ 📥 | `import` | | ⬆ 📤 | `export` |
| 📎 | `paperclip` | | ⋯ | `more` |
| ⚠ | `danger` | | ℹ | `info-circle` |
| 🔔 | `notification` | | 🛒 | `shopping-cart` |
| + | `add` | | | |

Nút Nhập/Xuất Excel dùng `document-upload` / `document-download`.

## 5. Tỉ lệ và vị trí

Wireframe không theo tỉ lệ thật. **Không nhân tọa độ.** Chỉ dùng tọa độ để biết:
- thứ tự trên–dưới, trái–phải của phần tử;
- phần tử nào cùng hàng (chênh lệch y < 12) → cùng một auto layout ngang;
- phần tử căn trái hay căn phải trong vùng (nằm ở nửa phải → căn phải, vd nút footer);
- độ rộng tương đối của cột bảng (dùng làm tỉ lệ, rồi làm tròn theo lưới 4).

Kích thước thật lấy từ kích thước biến thể trong `design-kit.md`, kích thước màn chuẩn trong `design.md` của kit, và màn tham chiếu cùng loại trong file đích.

## 6. Luồng → hành động và prototype

- Mỗi luồng `A → B «nhãn»`: màn A phải có nút hoặc link khớp nhãn (bỏ phần trong ngoặc). Không tìm thấy → báo, có thể nút nằm trong vùng chưa vẽ.
- Luồng tới cùng một màn đích với điều kiện khác nhau (`Cân bằng kho (còn dòng chưa kiểm)` / `(đã kiểm hết)`) là **một nút, hai kết quả**. Vẽ một nút; điều kiện ghi vào log để đưa sang SRS.
- Nhãn luồng không gắn mũi tên (vd `Lưu tạm → phiếu Chưa xử lý`) là mô tả kết quả: tìm nút tương ứng ở màn nguồn; kết quả thường là một Toast + quay về danh sách.
- Người dùng muốn prototype → nối `On click` từ nút sang frame đích; popup dùng `Open overlay` căn giữa, nền scrim.
