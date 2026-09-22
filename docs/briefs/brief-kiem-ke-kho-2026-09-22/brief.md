---
title: Kiểm kê kho — Giải pháp sơ bộ
type: preliminary-solution
stage: 1
feature: kiem-ke-kho
status: draft
lang: vi
owner: "[ASSUMPTION] BA phụ trách nghiệp vụ kho"
audience: PO, PM
created: 2026-09-22
updated: 2026-09-22
source: "Nhu cầu chung của tệp khách POS; tổng hợp từ yêu cầu người dùng v2, SPEC-kiem-ke-kho và khảo sát Sapo · KiotViet · CukCuk (2026-09-21)"
changelog:
  - 2026-09-22 | tạo giải pháp sơ bộ, bám theo SPEC-kiem-ke-kho
---

# Kiểm kê kho — Giải pháp sơ bộ

> **Tóm tắt cho PO/PM.** Phần mềm POS hiện chưa có nghiệp vụ kiểm kê, nên khách hàng phải đếm tay, ghi Excel rồi sửa tồn qua những đường không để lại dấu vết. Đề xuất: làm một nghiệp vụ kiểm kê **gọn** gồm tạo đợt → đếm → đối chiếu → cân bằng kho, với **một điểm khác biệt duy nhất nhưng quan trọng**: *cửa hàng vẫn bán hàng trong lúc kiểm mà chênh lệch vẫn đúng*. Cả ba đối thủ đều không có tài liệu nào nói về điểm này.

## 1. Làm rõ yêu cầu

### 1.1 Chân dung khách hàng
Khách hàng bán lẻ dùng POS, gồm **cửa hàng đơn lẻ** và **chuỗi nhiều cửa hàng**, quy mô tới khoảng 20.000 mã hàng/kho, có một phần hàng quản lý theo lô – hạn dùng. Họ cần đối chiếu tồn hệ thống với tồn thực tế định kỳ hoặc khi nghi có thất thoát. Việc kiểm kê diễn ra ngay tại cửa hàng/kho, thường vào buổi tối hoặc giờ vắng khách, và **cửa hàng không đóng cửa để đếm**.
`[ASSUMPTION]` Ngành hàng chính là tạp hóa/mini-mart và bán lẻ tổng hợp. Nhà thuốc nằm ngoài phase này.

### 1.2 Câu chuyện nghiệp vụ
Hiện nay, khi đến kỳ đóng sổ hoặc khi thấy số tồn "có vẻ sai", quản lý cửa hàng in danh sách hàng, chia người đếm trên giấy, gõ lại vào Excel để so với tồn trên phần mềm, rồi sửa tồn từng mã bằng phiếu nhập/xuất tay.
Quy trình hiện tại: In danh sách → Đếm trên giấy → Gõ lại Excel, so chênh lệch → Sửa tồn thủ công từng mã → Gửi số cho kế toán gõ lại.

### 1.3 Mức độ phần mềm hiện đáp ứng
Phần mềm đã có danh mục kho, phân quyền, giá vốn, quản lý lô – hạn dùng và máy quét mã vạch tại quầy. Tuy nhiên phần mềm **chưa có nghiệp vụ kiểm kê**: chưa có phiếu kiểm kê, chưa có bảng đối chiếu, và chưa có cách hợp lệ để điều chỉnh tồn theo kết quả đếm.

### 1.4 Vấn đề gặp phải
- **Quản lý / thủ kho** mất nhiều công gõ lại số. Đếm trùng kệ, nhầm đơn vị (thùng thay vì lon) và file Excel sai cột là những lỗi thường gặp.
- **Thủ kho bị quy trách nhiệm oan.** Hàng bán trong lúc đếm hiện ra thành "thiếu", vì không ai biết số tồn đem ra so là tồn ở thời điểm nào.
- **Kế toán** không có căn cứ đóng sổ. Chênh lệch không được quy ra tiền, và kế toán phải hạch toán lại bằng tay.
- **Chủ shop** không biết thực sự còn bao nhiêu tiền nằm trong kho. Tồn bị sửa tự do nên thất thoát chỉ lộ ra khi đã thành thói quen.

### 1.5 Kết quả mong muốn
Chủ shop và quản lý muốn phần mềm hỗ trợ **kiểm kê ngay trên hệ thống trong khi vẫn bán hàng**, cho ra chênh lệch đúng theo cả số lượng lẫn tiền, rồi cân bằng tồn bằng một thao tác có phân quyền và có dấu vết, **để sáng hôm sau mở bán với số tồn tin được** mà không phải đối chiếu lại bằng Excel.

## 2. Yêu cầu nghiệp vụ

Hệ thống phải hỗ trợ trọn một vòng kiểm kê trên POS, từ lúc tạo đợt tới khi cân bằng kho. Yêu cầu chia thành bốn nhóm:

### 2.1 Lập đợt và chốt tồn
- **Tạo đợt theo phạm vi:** kiểm toàn kho, hoặc theo ngành/nhóm hàng, theo nhà cung cấp, theo danh sách mã chọn tay. Nhờ vậy không phải đếm cả kho chỉ để kiểm một nhóm.
- **Chặn đợt chồng lấn:** không cho hai đợt đang mở trùng mã trên cùng một kho, tránh điều chỉnh hai lần cho cùng một chênh lệch.
- **Bán hàng không bị gián đoạn:** POS không bị khóa ở bất kỳ thời điểm nào. Mỗi dòng đếm ghi lại tồn hệ thống **tại đúng lúc đếm dòng đó**, nên đơn bán sau đó không làm sai chênh lệch.
- **Mốc thời điểm của đợt (T0):** in trên phiếu và mọi báo cáo; dùng làm cơ sở cho các mã chưa được đếm.

### 2.2 Đếm
- **Nhập bằng quét mã hoặc gõ tay** trên một màn hình không cần đào tạo; có hiển thị tồn hệ thống bên cạnh, có tiến độ, số đã nhập không bị mất.
- **Chọn đơn vị tính** (thùng/lốc/lon), hệ thống tự quy đổi về đơn vị tồn. **Quét trùng** thì cộng dồn hoặc cảnh báo, không âm thầm ghi đè.
- **Nhập từ Excel** cho cửa hàng đếm trên giấy: có bước xem trước dòng lỗi, và khai được thời điểm đếm thực tế cho cả lô dữ liệu.
- **Đếm theo lô – hạn dùng** với hàng có quản lý lô.

### 2.3 Đối chiếu và cân bằng kho
- **Bảng đối chiếu** hiển thị tồn hệ thống, số thực đếm, chênh lệch số lượng và **chênh lệch quy ra tiền** (theo giá vốn tại thời điểm cân bằng), lọc/sắp xếp được để xử lý dòng lớn trước.
- **Tách "chưa đếm" khỏi "đếm ra 0":** khi cân bằng mà còn mã chưa đếm, hệ thống hỏi người dùng muốn *bỏ qua (giữ nguyên tồn)* hay *quay lại đếm*. Không bao giờ tự đưa về 0.
- **Lý do lệch** nhập cho từng dòng.
- **Cân bằng kho** tự sinh chứng từ điều chỉnh tăng/giảm (ở mức lô nếu có lô, chỉ tác động kho được kiểm), không ai phải gõ lại số.

### 2.4 Kiểm soát và lưu vết
- **Sáu quyền độc lập:** tạo · xem · sửa · cân bằng kho · in · nhập Excel. **Quyền cân bằng kho là chốt kiểm soát duy nhất.** Không có bước duyệt phiếu.
- **Hai trạng thái phiếu:** *Chưa xử lý* (không tác động tồn, xóa được) → *Đã xử lý* (bất biến, không sửa, không hủy, không xóa).
- **Nhật ký thay đổi, biên bản PDF, tra cứu lịch sử** theo cửa hàng, kỳ và người thực hiện.

**Mục tiêu:** một cửa hàng 20.000 mã kiểm xong toàn kho trong **một buổi tối** khi POS vẫn bán. Chênh lệch cuối cùng giải thích được đến từng đồng, và mọi phiếu đã xử lý truy ngược được về từng dòng đếm.
`[ASSUMPTION]` Chưa có chỉ số đo sau khi ra mắt, ví dụ tỷ lệ cửa hàng chạy ít nhất một đợt kiểm kê trong 30 ngày đầu. PO/PM cần chốt chỉ số này.

## 3. Giải pháp nghiệp vụ

Xây dựng tính năng **"Kiểm kê kho"** trong nhóm nghiệp vụ Kho của POS. Tính năng dùng lại danh mục kho, phân quyền, giá vốn và quản lý lô sẵn có, **không dựng hệ thống song song**.

**Thành phần giải pháp:**
- **Giao diện:** thêm danh sách phiếu kiểm kê, màn hình đếm (quét/gõ, dùng được trên điện thoại qua web) và màn hình đối chiếu có nút *Cân bằng kho*.
- **Logic xử lý:**
  - Chênh lệch của từng dòng được "đóng băng" tại thời điểm đếm, lấy từ sổ chuyển động tồn kho: mọi chứng từ tác động tồn đều tự động được tính, kể cả loại chứng từ sinh thêm về sau.
  - Chặn ghi lùi ngày vào khoảng thời gian có phiếu đang mở.
  - Giá trị lệch tính theo giá vốn tại lúc cân bằng.
- **Quy trình:** Tạo đợt & chọn phạm vi → Đếm (quét / gõ / import Excel) → Xem đối chiếu, nhập lý do lệch → Cân bằng kho (người có quyền) → Lưu biên bản, tra cứu.

**Phạm vi ảnh hưởng:**
- **Bán hàng, nhập hàng, chuyển kho, trả hàng, hủy hàng:** không đổi luồng. Chỉ bị chặn *ghi lùi ngày* khi có phiếu kiểm kê đang mở. Chuyển kho chỉ tính vào kho nhận khi bên nhận ghi nhận.
- **Giá vốn và báo cáo tồn:** thay đổi theo chứng từ điều chỉnh do kiểm kê sinh ra.
- **Phân quyền:** thêm sáu quyền mới vào vai trò.
- **Nền tảng:** web; màn hình đếm dùng responsive trên điện thoại, quét bằng camera. `[ASSUMPTION]` Chưa làm app native và chưa hỗ trợ offline trong phase này.

**Ngoài phạm vi phase này:**
- Kiểm tới serial/IMEI, size–màu, vị trí kệ; hàng không nằm trong kho.
- Đếm mù; luồng duyệt phiếu; ghi nhận mã lạ khi đếm; đếm lại theo ngưỡng.
- Báo cáo tỷ lệ chính xác tồn; nghiệp vụ nhà thuốc / liên thông CSDL Dược.

**Định vị so với đối thủ:**
- Về luồng cơ bản, sản phẩm **ngang bằng** KiotViet và Sapo.
- Điểm hơn là **đúng khi bán xen giữa**, sáu quyền thay vì hai, và có lý do lệch.
- Đếm mù và luồng duyệt từng là khoảng trống cạnh tranh nhưng đã **chủ động cắt**.
