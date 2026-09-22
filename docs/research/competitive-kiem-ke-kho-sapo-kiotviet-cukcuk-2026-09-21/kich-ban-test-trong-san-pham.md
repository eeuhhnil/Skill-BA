# Kịch bản test trong sản phẩm — KiotViet & Sapo

> Mục đích: lấy bằng chứng **primary** về nghiệp vụ kiểm kê kho của đối thủ, thứ mà tài liệu công khai không nói.
> Cách dùng: chạy lần lượt trên từng sản phẩm, điền vào cột trả lời, gửi lại file này (hoặc ảnh chụp màn hình).
> Thời gian ước tính: 15–20 phút mỗi sản phẩm.
> Ngày chạy: ............

**Lưu ý trước khi bắt đầu:** nên dùng dữ liệu thử, tránh thao tác trên hàng hoá thật đang kinh doanh. Riêng test số 1 và số 3 có sinh phiếu và có thể chạm vào tồn kho — cân nhắc huỷ phiếu sau khi test xong.

---

## Test 1 — Snapshot / cut-off ⭐ QUAN TRỌNG NHẤT

**Thao tác:**
1. Ghi lại tồn hệ thống của một mã hàng X. Tồn ban đầu: ............
2. Tạo một phiếu kiểm kê có chứa mã X. **Để nguyên phiếu đó, chưa nhập gì.**
3. Sang màn hình bán hàng (POS), bán 1 đơn có mã X.
4. Quay lại phiếu kiểm kê đang mở, nhìn cột tồn hệ thống của mã X.

**Câu hỏi:** Số tồn hệ thống trên phiếu có thay đổi không?

| | KiotViet | Sapo |
|---|---|---|
| Tồn trên phiếu sau khi bán | | |
| → Có snapshot? (Không đổi = CÓ) | | |
| Hệ thống có cảnh báo gì không? | | |

---

## Test 2 — Đếm mù

**Thao tác:** Mở phiếu kiểm kê, vào màn hình nhập số đếm.

**Câu hỏi:** Màn hình có hiện sẵn số tồn hệ thống ngay cạnh ô nhập không?

| | KiotViet | Sapo |
|---|---|---|
| Có hiện tồn hệ thống? | | |
| Có tuỳ chọn ẩn đi không? | | |

---

## Test 3 — Mã chưa đếm ⭐ QUAN TRỌNG NHẤT

**Thao tác:** Tạo phiếu có khoảng 15 mã. Chỉ nhập số đếm cho 5 mã. Bấm hoàn thành / cân bằng kho.

**Câu hỏi:** 10 mã chưa đếm bị xử lý thế nào?

| | KiotViet | Sapo |
|---|---|---|
| Bị coi là tồn 0? | | |
| Giữ nguyên tồn cũ? | | |
| Hệ thống có hỏi lại / cảnh báo không? | | |
| Có cho chọn không? | | |

---

## Test 4 — Lô / hạn sử dụng

**Thao tác:** Tìm một mã hàng có quản lý lô–hạn dùng (nếu có), đưa vào phiếu kiểm kê.

| | KiotViet | Sapo |
|---|---|---|
| Có cột lô riêng để đếm? | | |
| Có cột hạn dùng? | | |
| Hay chỉ đếm tổng theo mã hàng? | | |
| Sửa được hạn dùng ngay khi đếm? | | |

---

## Test 5 — Duyệt & khoá sau khi chốt

| | KiotViet | Sapo |
|---|---|---|
| Phiếu có những trạng thái nào? | | |
| Có bước chờ duyệt không? | | |
| Sau khi hoàn thành còn sửa được không? | | |
| Người đếm và người chỉnh tồn có tách quyền không? | | |
| Có xem được lịch sử ai sửa gì không? | | |

---

## Test 6 — Bảng chênh lệch

| | KiotViet | Sapo |
|---|---|---|
| Có cột giá trị tiền không? | | |
| Có phân loại lý do lệch không? | | |
| Lọc được chỉ xem mã bị lệch không? | | |
| Xuất được file không? | | |

---

## Test 7 — Nhập từ Excel

| | KiotViet | Sapo |
|---|---|---|
| Có chức năng import không? | | |
| Có màn hình xem trước không? | | |
| Có báo dòng lỗi trước khi ghi không? | | |
| Import đè hay cộng dồn vào số đã đếm? | | |

---

## Test 8 — Trên điện thoại

| | KiotViet | Sapo |
|---|---|---|
| Mở được phiếu kiểm kê trên app/mobile? | | |
| Quét mã bằng camera được không? | | |
| Dùng được khi mất mạng không? | | |

---

## Quan sát thêm (tuỳ ý, rất có giá trị)

- Có kiểm kê theo khu vực / nhóm hàng / một phần kho không? ............
- Nhiều người đếm cùng lúc trên một phiếu được không? ............
- Có báo cáo lịch sử các lần kiểm kê không? ............
- Điều gì làm anh/chị thấy khó chịu nhất khi dùng thử? ............
- Điều gì làm tốt hơn mong đợi? ............
