# Pos — ghi chú cho người vẽ

Phần viết tay đi kèm `design-kit.md` (file máy sinh, không sửa tay). Sinh lại kit không đụng tới file này.

## Nguồn

| | |
|---|---|
| Sản phẩm | EasyPOS |
| File Figma nguồn | **Pos** |
| Link | _(điền link file Pos)_ |
| Page chứa design system | `Design system` |
| Collection token dùng để vẽ | `Pos Design Tokens` |
| Font | Poppins (text style `heading/*`, `title/*`, `body/*`) |
| Kích thước web chuẩn | 1440×900 |

## Vẽ ở file khác file Pos

Id component trong kit chỉ dùng được bên trong file Pos. Vẽ ở file khác thì phải import theo `key` (`get_library_component`), và chỉ chạy được khi Pos đã được publish thành library và đã bật trong file đích. File Pos đang ở gói Starter nên chưa publish được.

## Bẫy riêng của file này

- **Input Dropdown / Input đặt nhãn bên trái trong cột ~66px** → nhãn dài bị cắt. Nhãn ngắn ("Kho hàng", "Ghi chú") thì giữ; nhãn dài → ẩn lớp nhãn trái của instance (`I<instance>;1544:59431` với Input Dropdown `1544:59429`) và đặt nhãn riêng phía trên.
- **Button hiện icon trái/phải mặc định** → ẩn các INSTANCE con trực tiếp, resize về 120×40.
- **Bảng dựng từ set `Table` rộng 1546–1586px**: resize từng ô (instance) theo mảng độ rộng; cột số giữ ≥ 112px. Bảng dài → `primaryAxisSizingMode:"FIXED"`, `clipsContent:true`, đặt chiều cao vừa khung để nút hành động không bị đẩy khỏi 900px.
- **`design_fingerprint` và `get_components` toàn file luôn timeout** (~6.3k component icon) — đừng gọi. Đọc theo khung.
- **File rất lớn**: không đọc cả page; đọc theo node/khung.
- **Gói Starter: tối đa 3 page** → không tạo page mới.
