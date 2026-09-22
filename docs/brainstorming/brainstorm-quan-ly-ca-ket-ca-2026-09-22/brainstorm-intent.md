# Intent: Quản lý ca, kết ca

## 1. Bối cảnh & mục tiêu

Nghiệp vụ quản lý ca làm việc và kết ca (mở ca, giao dịch trong ca, đóng ca) của cửa hàng bán lẻ. Mục tiêu brainstorm: xác định pain point và nhu cầu người dùng thực sự đối với nghiệp vụ này, làm đầu vào cho các bước lập kế hoạch tiếp theo.

## 2. Vai liên quan

- Nhân viên bán hàng/thu ngân — người trực tiếp mở ca, thao tác trong ca, kết ca.
- Quản lý cửa hàng — theo dõi, kiểm soát ca làm việc của nhân viên, giải trình với chủ cửa hàng.
- Chủ cửa hàng — xem tổng quan vận hành/doanh thu, không đi sâu chi tiết từng ca.

## 3. Pain points chính theo từng vai

**Thu ngân**
- Sợ chênh lệch tiền mặt lúc kết ca.
- Sợ nhận bàn giao số dư sai từ ca trước, bị đổ lỗi oan cho lệch quỹ không phải do mình.
- Sợ trong ca đông khách, thao tác nhầm/không kịp ghi chép khoản tiền mặt phát sinh, dồn thành lệch khó giải thích cuối ca.

**Quản lý cửa hàng**
- Sợ bị chủ cửa hàng đổ trách nhiệm ngược khi không có đủ dữ liệu/bằng chứng theo từng ca để giải trình thất thoát.
- (Ghi nhận nhưng ngoài phạm vi lần này) Sợ thiếu người trực ca đột xuất, không kịp sắp người thay — thuộc nghiệp vụ lịch phân ca/roster khác.

**Chủ cửa hàng**
- Cần nắm nhanh tình hình vận hành mà không cần tự đi hỏi từng quản lý.
- (Đã loại) Ý "sợ quản lý và nhân viên che giấu lẫn nhau" — user xác nhận không phù hợp quy mô/bối cảnh hiện tại, không đưa vào scope.

## 4. Root cause quan trọng (Five Whys)

Chênh lệch tiền mặt (đặc biệt do trả tiền thừa nhầm cho khách) bắt nguồn từ: toàn bộ việc đếm tiền mặt vật lý (kể cả tiền thừa trả khách) đều làm thủ công bằng tay, không có công cụ/bước hỗ trợ kiểm tra — dưới áp lực thời gian khi khách đông, dễ đếm nhầm số lượng/mệnh giá dù hệ thống đã tính sẵn số tiền thừa cần trả.

Đây là khoảng trống chưa được giải quyết: danh sách MUST/SHOULD hiện tại chỉ xử lý hậu quả của chênh lệch (ghi lý do, in phiếu, tra cứu), chưa có gì phòng ngừa root cause này. Cần brainstorm/thiết kế riêng cho phase sau.

## 5. Nhu cầu/chức năng đã chốt (MoSCoW)

**MUST**
- Mở ca: nhập số tiền mặt đầu ca.
- Trong ca: xem tiền mặt đầu ca và tiền mặt hiện tại (chỉ xem, không thêm thao tác ghi chép mới).
- Kết ca: nhập số tiền mặt thực tế, ghi lý do khi có chênh lệch, in phiếu kết ca.
- Danh sách ca làm việc: hồ sơ chi tiết từng ca (ai mở/đóng, số tiền đầu ca/trong ca/kết ca, chênh lệch, lý do), lọc theo khoảng thời gian, trạng thái (đang diễn ra/đã đóng), nhân viên — dùng để tra cứu/giải trình bất cứ lúc nào.

**SHOULD**
- Đính kèm ảnh chứng từ/biên lai khi ghi lý do chênh lệch.

**WON'T THIS TIME**
- Cảnh báo/xác nhận lệch quỹ tự động.
- Đối chiếu với ca trước lúc mở ca.
- Báo cáo doanh thu tổng hợp.

**NGOÀI PHẠM VI**
- Tạm ứng/thu chi trong ca — đã có sẵn ở mục "Lập phiếu chi" của phần mềm hiện tại.
- Lịch phân ca/thiếu người trực ca — thuộc nghiệp vụ khác (roster), để brainstorm riêng sau.

## 6. Insight tổng hợp cần giữ lại

- Job-to-be-done chung của tính năng kết ca/hồ sơ ca: mang lại "bằng chứng và niềm tin" — thu ngân cần bằng chứng không thể chối cãi để tự bảo vệ mình khỏi bị quy trách nhiệm oan; quản lý cần dữ liệu chi tiết để giải trình và chứng minh mình kiểm soát tốt; chủ cửa hàng cần yên tâm mọi thứ đang chạy tốt mà không cần hỏi trực tiếp. Đây không phải bài toán nhập liệu đơn thuần.
- Vì bản chất là "bằng chứng", phiếu kết ca và hồ sơ ca (danh sách ca làm việc) nên được thiết kế như bằng chứng không thể chối cãi (đầy đủ, minh bạch, tra cứu được mọi lúc) chứ không chỉ là form nhập liệu.
- "Thiếu người trực ca" là nhu cầu thật của quản lý cửa hàng nhưng thuộc module lịch phân ca/roster khác với quản lý ca/kết ca — để dành brainstorm riêng ở phase sau, không gộp vào scope này.
