# Đọc wireframe Excalidraw và chuyển sang component

## 1. Đọc file

```
python {skill-root}/scripts/read_excalidraw.py <file.excalidraw>          # bản đọc cho người
python {skill-root}/scripts/read_excalidraw.py <file.excalidraw> --json   # khi cần tọa độ để dựng
```

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

| Trên wireframe | Component | Ghi chú |
|---|---|---|
| Ô có nền `#dee2e6` + chữ động từ | Button L Primary | Mỗi vùng chỉ có một nút Primary |
| Ô viền, không nền + chữ động từ | Button L Secondary | `Hủy`, `Quay lại`, `Nhập Excel`… |
| Chữ bắt đầu bằng `+` | Button có icon `Plus` | Bỏ dấu `+` khỏi nhãn |
| Ô dài có chữ xám | Input, chữ xám = placeholder | Có `🔍` → Search field |
| Chữ + `▾` trong ô | Select | `Lọc ▾` → Button Secondary có `ChevronDown` hoặc Select |
| Chữ + `📅` hoặc dạng ngày trong ô | Date picker | `01/09 – 22/09` → khoảng ngày, viết đủ năm |
| Nhãn có ` *` phía trên ô | Input `Required` | |
| `(khóa)` sau giá trị | Input Disabled / read-only | Bỏ chữ `(khóa)`, giữ giá trị |
| `Kho: Kho chính` (nhãn: giá trị, không có ô) | Cặp nhãn–giá trị chỉ đọc | `Label` + `Title/sm` |
| `○ … ● …` | Radio group | `●` = đang chọn |
| `☐` / `☑` | Checkbox Off / On | Ở cột đầu bảng → cột chọn |
| `[Tất cả 3] [Chưa kiểm 1] …` | Chip lọc có số đếm | Phần tử đầu = Active |
| `(1) Bước A ───── (2) Bước B`, `✓` = xong | Stepper các bước | |
| Hàng ô liền nhau + kẻ `#ced4da` | Data table | Hàng đầu = header; dòng đầu có chữ thường là dữ liệu mẫu |
| Ô nhỏ trong dòng bảng | Input cao 32 trong bảng | Cột số → căn phải |
| `↳ [Chọn lô] (hàng có lô)` | Dòng con + link `Chọn lô` | Giống add-on row của giỏ hàng |
| `Chưa xử lý`, `Đã xử lý`… trong cột trạng thái | Tag | Chưa xử lý = Amber, Đã xử lý/Hoàn thành = Green, Hủy = Red, Nháp = Gray |
| `‹ 1 2 3 ›`, `50 bản ghi/trang` | Pager | |
| Ô lớn, trống, dưới nhãn `Ghi chú…` | Textarea [suy ra: Input nhiều dòng, cao 80] | |
| Khung nhỏ hơn màn, có thanh tiêu đề | Modal trên màn nguồn | Rộng theo `layouts.md` §4 |
| Dòng chữ xám dài giải thích quy tắc | **Chú thích cho người đọc**, không vẽ | Đưa vào log để chuyển sang SRS |

Không chắc một dòng chữ là UI hay chú thích → không vẽ, ghi vào câu hỏi mở.

## 4. Emoji → icon

| Emoji | Lucide | | Emoji | Lucide |
|---|---|---|---|---|
| 🔍 | `Search` | | ✎ ✏️ | `SquarePen` |
| 🗑 | `Trash2` | | 🖨 | `Printer` |
| 📅 | `Calendar` | | ☰ | `Menu` |
| ▾ | `ChevronDown` | | ‹ › | `ChevronLeft` / `ChevronRight` |
| ✕ ✖ | `X` | | ✓ ✔ | `Check` |
| ⚙ | `Settings` | | 👁 | `Eye` |
| ⬇ 📥 | `Download` | | ⬆ 📤 | `Upload` |
| 📎 | `Paperclip` | | ⋯ | `Ellipsis` |
| ⚠ | `TriangleAlert` | | ℹ | `Info` |
| 🔔 | `Bell` | | 🛒 | `ShoppingCart` |

Nút Nhập/Xuất Excel dùng `FileUp` / `FileDown`.

## 5. Tỉ lệ và vị trí

Wireframe không theo tỉ lệ thật. **Không nhân tọa độ.** Chỉ dùng tọa độ để biết:
- thứ tự trên–dưới, trái–phải của phần tử;
- phần tử nào cùng hàng (chênh lệch y < 12) → cùng một auto layout ngang;
- phần tử căn trái hay căn phải trong vùng (nằm ở nửa phải → căn phải, vd nút footer);
- độ rộng tương đối của cột bảng (dùng làm tỉ lệ, rồi làm tròn theo lưới 4).

Kích thước thật lấy từ `layouts.md` và `components.md`.

## 6. Luồng → hành động và prototype

- Mỗi luồng `A → B «nhãn»`: màn A phải có nút hoặc link khớp nhãn (bỏ phần trong ngoặc). Không tìm thấy → báo, có thể nút nằm trong vùng chưa vẽ.
- Luồng tới cùng một màn đích với điều kiện khác nhau (`Cân bằng kho (còn dòng chưa kiểm)` / `(đã kiểm hết)`) là **một nút, hai kết quả**. Vẽ một nút; điều kiện ghi vào log để đưa sang SRS.
- Nhãn luồng không gắn mũi tên (vd `Lưu tạm → phiếu Chưa xử lý`) là mô tả kết quả: tìm nút tương ứng ở màn nguồn; kết quả thường là một Toast + quay về danh sách.
- Người dùng muốn prototype → nối `On click` từ nút sang frame đích; popup dùng `Open overlay` căn giữa, nền scrim.
