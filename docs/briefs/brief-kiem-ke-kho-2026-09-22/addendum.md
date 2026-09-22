---
title: Kiểm kê kho — Phụ lục giải pháp sơ bộ
created: 2026-09-22
updated: 2026-09-22
---

# Phụ lục — Kiểm kê kho

Chi tiết dành cho PRD và đặc tả, không đưa vào thân brief.

## A. Các phương án đã cân nhắc và bị bác

| Phương án | Kết luận | Lý do |
|---|---|---|
| Chốt snapshot cấp đợt rồi "tua ngược" giao dịch phát sinh (YC-13 bản v2) | Bác, thay bằng chốt tồn tại thời điểm đếm từng dòng (QT-2) | Đằng nào cũng cần mốc thời gian từng dòng, nên tua ngược là thừa. Cách chốt từng dòng giải thích được bằng một câu cho thủ kho |
| Liệt kê cứng các loại chứng từ được tính vào tồn | Bác | Loại chứng từ mới về sau sẽ bị bỏ sót, gây tồn sai âm thầm |
| Đếm mù | Cắt (QĐ 1) | Theo thông lệ thị trường. Là chỗ quay lại nếu phát sinh nhu cầu chống gian lận nội bộ |
| Luồng duyệt phiếu (YC-53/54/55) | Cắt (QĐ 2) | Thay bằng sáu quyền; quyền cân bằng kho là chốt kiểm soát |
| Ghi nhận mã lạ khi đếm (CAP-7) | Cắt | Phase sau, nếu mở lại cho nhà thuốc, sẽ xung đột với CSDL Dược |
| Đếm lại theo ngưỡng lệch (CAP-11) | Cắt | — |
| Báo cáo tỷ lệ chính xác tồn (CAP-16) | Cắt | Gắn với nhu cầu "yên tâm theo thời gian" của chủ shop; ứng viên mạnh cho phase 2 |

## B. Bối cảnh đối thủ (khảo sát 2026-09-21)

- **KiotViet:** hai trạng thái Phiếu tạm → Đã cân bằng kho; bấm Hoàn thành là tồn đổi ngay. Tài liệu không nói gì về phân quyền.
- **Sapo:** chỉ hai quyền (xem / tạo), ai tạo được phiếu cũng cân bằng được. Mã chưa đếm: hỏi người dùng (nguồn chưa xác nhận lại được). Có lỗi: đưa lô về 0 thì giá vốn lô bị reset về 0.
- **CukCuk:** có bước Xử lý sinh chứng từ Nhập/Xuất kho kiểm kê riêng; là đối thủ duy nhất có trường lý do lệch.
- **Cả ba:** không có tài liệu nào nói về snapshot/cut-off, và không trang nào dặn người dùng đừng bán hàng khi đang kiểm. Không đối thủ nào có đếm mù.
- **Caveat:** dựa chủ yếu vào tài liệu vendor tự công bố. Kịch bản kiểm chứng trực tiếp nằm ở `docs/research/.../kich-ban-test-trong-san-pham.md`.

## C. Ứng viên cho phase sau

Đếm song song nhiều người / chia phiếu con · tạm dừng nhập-xuất thủ công khi đếm · đánh dấu cận date/hỏng khi đếm · xuất bảng chênh lệch ra Excel · màn hình tổng hợp cho chủ chuỗi · báo cáo theo lý do lệch · kiểm kê luân phiên (nên mô hình hóa dữ liệu sẵn ngay từ đầu) · app offline · RFID/thiết bị ngoài · nghiệp vụ nhà thuốc.
