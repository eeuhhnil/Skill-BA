---
type: preliminary-solution
stage: 1
feature: quan-ly-ca-ket-ca
status: draft
lang: vi
owner: ""
created: 2026-09-22
updated: 2026-09-22
source: "Phiên brainstorming quản lý ca/kết ca (2026-09-22)"
changelog:
  - 2026-09-22 | created preliminary solution
---

# Quản lý ca, kết ca — Preliminary Solution

## 1. Làm rõ yêu cầu

### 1.1 Đối tượng khách hàng
Chủ cửa hàng/quản lý cửa hàng bán lẻ đang dùng EasyPOS cần quản lý việc mở ca, theo dõi và kết ca của nhân viên thu ngân — thực hiện tại module "Quản lý ca" (mới) trên EasyPOS bản Desktop.

### 1.2 Câu chuyện nghiệp vụ
Hiện tại, khi kết ca, thu ngân ghi tay số liệu lên giấy hoặc Excel rồi gửi cho quản lý cửa hàng. Quản lý xem nhưng không có đủ căn cứ (dữ liệu chi tiết, minh chứng) để đối chiếu số liệu đó đúng hay sai.

Quy trình hiện tại: Thu ngân ghi tay số liệu kết ca lên giấy/Excel → Gửi cho quản lý cửa hàng → Quản lý xem nhưng không đối chiếu/xác minh được vì thiếu căn cứ.

### 1.3 Phần mềm hiện đã hỗ trợ
EasyPOS đã hỗ trợ lập phiếu chi (ghi nhận khoản thu/chi phát sinh trong ca). Tuy nhiên, phần mềm chưa hỗ trợ mở ca/kết ca, ghi nhận tiền mặt đầu ca - kết ca, hay tra cứu/đối chiếu lịch sử ca làm việc.

### 1.4 Pain Points
- **Thu ngân** lo sợ chênh lệch tiền mặt lúc kết ca; sợ nhận bàn giao số dư sai từ ca trước và bị quy trách nhiệm oan; không kịp ghi chép phát sinh khi khách đông, dồn thành khoản lệch khó giải thích cuối ca.
- **Quản lý cửa hàng** không có đủ dữ liệu/bằng chứng theo từng ca để giải trình với chủ cửa hàng khi có thất thoát — hệ quả trực tiếp của quy trình giấy/Excel hiện tại.
- **Gốc rễ của chênh lệch tiền mặt:** việc đếm tiền mặt vật lý (kể cả tiền thừa trả khách) hoàn toàn thủ công, không có công cụ hỗ trợ, dễ sai dưới áp lực thời gian khi đông khách. *(Ghi nhận là khoảng trống, chưa giải quyết trong scope stage 1 này.)*

### 1.5 Kết quả mong muốn
- **Thu ngân** muốn có bằng chứng rõ ràng, không thể chối cãi về số tiền đã bàn giao mỗi ca, để tự bảo vệ mình khi có tranh chấp/chênh lệch.
- **Quản lý cửa hàng** muốn dữ liệu số hóa theo từng ca (thay cho giấy/Excel), đủ căn cứ để đối chiếu và giải trình khi cần.
- **Chủ cửa hàng** muốn nắm nhanh tình hình vận hành mà không cần tự đi hỏi từng quản lý.

## 2. Yêu cầu nghiệp vụ

Hệ thống cần hỗ trợ số hóa toàn bộ vòng đời một ca làm việc (mở ca → trong ca → kết ca) và cung cấp dữ liệu đối chiếu/giải trình cho quản lý cửa hàng, thay thế quy trình ghi giấy/Excel hiện tại. Yêu cầu chia thành 4 nhóm:

### 2.1 Mở ca
- **Nhập tiền mặt đầu ca:** thu ngân nhập số tiền mặt thực tế có trong quầy khi bắt đầu ca, làm mốc đối chiếu cho lúc kết ca.

### 2.2 Trong ca
- **Xem tiền mặt trong ca:** thu ngân xem được số tiền mặt đầu ca và số tiền mặt hiện tại trong ca (chỉ xem, không phát sinh thao tác ghi chép mới) để chủ động theo dõi trong lúc bán hàng.

### 2.3 Kết ca
- **Nhập tiền mặt kết ca:** thu ngân nhập số tiền mặt kiểm đếm thực tế khi kết thúc ca.
- **Ghi lý do chênh lệch:** khi số tiền thực tế khác số tiền hệ thống ghi nhận, thu ngân ghi chú lý do, làm căn cứ đối chiếu sau này.
- **Đính kèm ảnh chứng từ:** thu ngân có thể đính kèm ảnh biên lai/chứng từ liên quan khi ghi lý do chênh lệch, tăng độ tin cậy của căn cứ.
- **In phiếu kết ca:** hệ thống in phiếu tổng hợp ca (đầu ca, kết ca, chênh lệch, lý do) để thu ngân bàn giao cho quản lý cửa hàng.

### 2.4 Quản trị / Báo cáo
- **Danh sách ca làm việc:** quản lý cửa hàng xem danh sách các ca, lọc theo khoảng thời gian, trạng thái (đang diễn ra/đã đóng), và theo nhân viên.
- **Chi tiết một ca:** quản lý cửa hàng xem chi tiết đầu ca/trong ca/kết ca/chênh lệch/chứng từ của một ca cụ thể để tra cứu, đối chiếu, giải trình với chủ cửa hàng bất cứ lúc nào.

**Mục tiêu:** 100% số liệu mở ca/kết ca được số hóa và lưu vết trên hệ thống, có căn cứ tra cứu/đối chiếu cho mọi ca — thay thế hoàn toàn quy trình ghi giấy/Excel hiện tại.

## 3. Giải pháp nghiệp vụ

Triển khai module "Quản lý ca" tích hợp vào luồng nghiệp vụ bán hàng của EasyPOS Desktop.

**Thành phần giải pháp:**
- **Giao diện (UI):** Thêm các màn hình Mở ca, Trong ca (xem), Kết ca cho thu ngân; và màn hình Danh sách ca / Chi tiết ca cho quản lý cửa hàng — trên EasyPOS bản Desktop.
- **Logic xử lý:**
  - *Tiền mặt trong ca* = tổng tiền mặt phát sinh trong ca (bán hàng tiền mặt + phiếu thu/chi đã lập), **không** cộng dồn với tiền đầu ca.
  - *Chênh lệch kết ca* = (Tiền đầu ca + Tiền phát sinh trong ca) − Tiền mặt thực tế nhập lúc kết ca.
  - Nếu chênh lệch khác 0, hệ thống yêu cầu thu ngân ghi lý do (có thể đính kèm ảnh chứng từ).
- **Quy trình:** Thu ngân mở ca (nhập tiền đầu ca) → Bán hàng/thu-chi phát sinh trong ca (hệ thống tự cộng dồn) → Thu ngân kết ca (nhập tiền thực tế, hệ thống tính chênh lệch, ghi lý do nếu có, in phiếu) → Quản lý tra cứu Danh sách ca/Chi tiết ca để đối chiếu, giải trình.

**Phạm vi ảnh hưởng:**
- Module "Lập phiếu chi" hiện có: dữ liệu thu/chi trong ca được tính vào công thức tiền mặt trong ca/chênh lệch.
- Module bán hàng: giao dịch bán hàng tiền mặt trong ca được tính vào công thức trên.
- Chỉ áp dụng cho EasyPOS bản Desktop ở giai đoạn này; chưa có phiên bản mobile/tablet riêng cho các vai.

## 4. Câu hỏi mở (cho cuộc họp duyệt Stage 2)

| # | Câu hỏi | Người trả lời | Trạng thái |
|---|---------|---------------|------------|
| 1 | Đính kèm ảnh chứng từ khi ghi lý do chênh lệch là bắt buộc hay tùy chọn? | PO | [ ] |
| 2 | Sau khi kết ca và in phiếu, phiếu/ca đó có được phép sửa lại không? Nếu có, ai được quyền sửa? | PO | [ ] |
| 3 | Gốc rễ chênh lệch (đếm tiền mặt thủ công, không có công cụ hỗ trợ) — có đưa vào roadmap phase sau không, hay chưa cần xử lý? | PO | [ ] |
| 4 | Ba hạng mục đã tạm hoãn ở brainstorm (cảnh báo/xác nhận lệch tự động, đối chiếu với ca trước lúc mở ca, báo cáo doanh thu tổng hợp) — có đưa vào roadmap ngay phase kế tiếp không? | PO | [ ] |
| 5 | Phiếu kết ca in ra: in giấy vật lý qua máy in hóa đơn, hay xuất PDF/lưu điện tử? | PO | [ ] |
