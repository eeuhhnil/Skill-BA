# Cách tìm ảnh hưởng: đi theo dòng dữ liệu

Từ khóa chỉ là công cụ. Điều giúp không sót là: **nghiệp vụ đọc gì → cái gì làm nó sai; nghiệp vụ ghi gì → ai đang dùng nó.**

Ví dụ xuyên suốt: **Kiểm kê kho**.

## Bước 1 — Nghiệp vụ chạm dữ liệu nào

| | Dữ liệu |
|---|---|
| **Đọc** | tồn hiện tại (kho, sản phẩm, lô), giá vốn, đơn vị tính, danh mục kho |
| **Ghi** | phiếu kiểm kê, phiếu nhập/xuất điều chỉnh, tồn kho mới |

Mỗi dòng là một hướng tìm.

## Bước 2 — Đã có tài liệu về chính nghiệp vụ này chưa (LÀM TRƯỚC TIÊN)

Từ khóa gồm tên gọi + đồng nghĩa + cách gọi của đối thủ: *"kiểm kê", "kiểm kho", "kiểm hàng", "cân bằng kho"*. Có đặc tả sẵn thì đọc nó đầu tiên — mục "Luồng ảnh hưởng" của nó là điểm xuất phát, và mọi khác biệt với tài liệu đầu vào phải nêu ở phần A.

## Bước 3 — Chiều "ghi": ai dùng thứ nghiệp vụ sinh ra (hay bị sót nhất)

| Hỏi | Từ khóa | Ví dụ |
|---|---|---|
| Ai phản ứng khi tồn thay đổi? | "đồng bộ tồn", "tồn thay đổi", "update_stock" | Shopee: tồn đổi → đẩy lên sàn |
| Ai đọc phiếu nhập/xuất? | "rs_inoutward", "phiếu xuất kho", "loại chứng từ" | Báo cáo XNT, CSDL Dược, EasyBooks |
| Ai tính lại theo phiếu kho? | "giá vốn", "tính giá xuất kho", "cogs" | Tính giá xuất kho bình quân cuối kỳ |
| Báo cáo nào dựa vào ngày chứng từ? | "tồn đầu kỳ", "kỳ báo cáo" | Ghi lùi ngày → báo cáo kỳ cũ đổi |

## Bước 4 — Chiều "đọc": cái gì làm dữ liệu đầu vào sai

| Hỏi | Từ khóa | Ví dụ |
|---|---|---|
| Cái gì làm tồn đổi trong lúc đếm? | "bán hàng", "trả hàng", "chuyển kho", "hủy hàng", "sản xuất" | Chuyển kho, lệnh sản xuất, liệu trình |
| Giao dịch nào về muộn? | "offline", "đồng bộ lại", "webhook" | Bán offline mobile, đơn Shopee |
| Tồn có thể âm / bị sửa ngoài luồng? | "xuất quá tồn", "sửa tồn", "điều chỉnh tồn" | Cho xuất quá tồn; sửa tồn theo lô trên màn sản phẩm |
| Hệ thống khác làm chủ dữ liệu? | "kết nối", "tích hợp", "ghép cặp" | EasyBooks, Shopee v1 |

## Bước 5 — Loại đối tượng đặc biệt

Với từng loại (*lô, hạn dùng, IMEI, serial, combo, định mức, liệu trình, đơn vị tính, biến thể*): **có dữ liệu riêng không, nghiệp vụ xử lý nó thế nào?** Ví dụ combo/thành phẩm định mức không có tồn riêng → loại khỏi kiểm kê; sản phẩm sản xuất có tồn riêng → phải kiểm được.

## Bước 6 — Phần bao quanh

Phân quyền ("phân quyền", "permission", "vai trò") · nền tảng ("mobile", "app", "offline") · mẫu in, cấu hình ("mẫu in", "cấu hình").

## Bước 7 — Đọc và phân loại

Với mỗi trang, chỉ trả lời:
1. **Có liên quan thật không?** (trang có chữ "tồn kho" nhưng nói chuyện khác → bỏ, ghi vào phần D)
2. **Mức độ:** High / Med / Low (theo quy ước trong mẫu)
3. **Ai xác nhận:** BA luồng đó / dev / PO

## Mẹo khi quét

- Loại các nhánh nhiễu (TestCase, Nâng cấp, Thay đổi giao diện…) nhưng ghi lại là đã loại.
- Trang xếp hạng cao chưa chắc quan trọng — trang đặc tả chính của nghiệp vụ có thể chỉ khớp 1–2 từ khóa.
- Để ý **mâu thuẫn ngay trong Confluence** (vd cùng một mã loại chứng từ ghi hai giá trị) — đưa vào phần C.
- Tài liệu mô tả thiết kế, không chắc là code đang chạy: điểm then chốt luôn gắn "cần dev xác nhận".
