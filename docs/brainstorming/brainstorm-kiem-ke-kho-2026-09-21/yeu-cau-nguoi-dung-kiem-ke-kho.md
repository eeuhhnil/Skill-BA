# Yêu cầu người dùng — Nghiệp vụ Kiểm kê kho

| | |
|---|---|
| **Tên nghiệp vụ** | Kiểm kê kho (đối chiếu tồn hệ thống với tồn thực tế và điều chỉnh tồn) |
| **Mục tiêu** | Cho phép cửa hàng xác định chính xác lượng hàng và giá trị hàng thực tế đang nằm trong kho/cửa hàng tại một thời điểm, phát hiện chênh lệch, và điều chỉnh tồn kho hệ thống theo một quy trình có kiểm soát, có phân quyền và có dấu vết. |
| **Bối cảnh sản phẩm** | Phần mềm **POS bán hàng** (không phải WMS, không phải ERP). Hiện phần mềm chưa có nghiệp vụ kiểm kê. Thiết bị quét mã vạch đã có sẵn tại quầy. Khách hàng có cả cửa hàng đơn lẻ và chuỗi nhiều cửa hàng. |
| **Ràng buộc nền tảng** | **POS vẫn tiếp tục bán hàng trong lúc kiểm kê.** Không được giả định cửa hàng đóng cửa để đếm. Vì vậy cơ chế chốt snapshot / cut-off là yêu cầu bắt buộc số một, không phải biện pháp phòng ngừa tùy chọn. |
| **Phiên bản** | **v2 — 2026-09-21.** v2 áp kết quả khảo sát đối thủ (Sapo, KiotViet, CukCuk) và 6 quyết định sản phẩm của BA. Bản v1 được giữ nguyên tại `yeu-cau-nguoi-dung-kiem-ke-kho.v1.bak`. |
| **Người đọc** | Business Analyst — dùng tài liệu này làm đầu vào viết tài liệu mô tả chức năng. |

---

## 0. Nhật ký quyết định — v1 → v2

Sáu quyết định sản phẩm ngày 2026-09-21, sau khi khảo sát Sapo, KiotViet và CukCuk. Ba trong số đó **bác lại khuyến nghị của báo cáo khảo sát**; lý do được ghi lại để người đọc sau hiểu vì sao.

| # | Quyết định | Ảnh hưởng | So với khuyến nghị khảo sát |
|---|---|---|---|
| 1 | **Không làm đếm mù.** Vẫn hiển thị tồn hệ thống như đối thủ | YC-33 đổi hẳn nội dung, từ *Nâng cao* → *Bắt buộc v1* | ❌ **Bác KN-1.** Khảo sát đề xuất nâng đếm mù lên vì không đối thủ nào có |
| 2 | **Không có bước duyệt phiếu.** Chỉ phân quyền: tạo · xem · sửa · cân bằng kho · in · import Excel | YC-51 viết lại thành 6 quyền; YC-50, YC-52 viết lại; **YC-53, YC-54, YC-55 bị loại bỏ**; YC-46, YC-49, YC-56, YC-60, YC-66 chỉnh theo | ❌ **Bác một phần KN-2.** Giữ tách quyền, bỏ luồng duyệt |
| 3 | **Mã chưa đếm: hiện thông báo cho người dùng chọn**, mặc định giữ nguyên tồn | YC-41 viết lại; **Quy tắc nghiệp vụ số 1 đã chốt** | ✅ Theo KN-3 (mô hình Sapo) |
| 4 | **Phase này chưa làm gì liên quan đến dược** | Chuyển sang mục 5 Ngoài phạm vi, kèm ghi chú xung đột với YC-27 để phase sau dùng lại | ❌ **Bác KN-4** cho phase này |
| 5 | **Có trường lý do lệch ở mỗi dòng** | YC-43 từ *Nên có* → *Bắt buộc v1* | ✅ Theo KN-8 |
| 6 | **Phiếu có hai trạng thái:** Chưa xử lý (mới lưu nháp) → Đã xử lý (đã cân bằng tồn kho) | YC-50 viết lại; YC-60, YC-66 chỉnh theo; **Quy tắc nghiệp vụ số 6 đã chốt** | — (không có khuyến nghị tương ứng) |
| 7 | **Hủy/xóa phiếu:** phiếu Chưa xử lý **xóa cứng**; phiếu Đã xử lý **không hủy, không xóa** | YC-06 viết lại; YC-64 thu hẹp phạm vi về phiếu Đã xử lý; xác nhận không có trạng thái "đã hủy" | — (không có khuyến nghị tương ứng) |

**Hệ quả cần biết:** quyết định 1, 2 và 6 cộng lại đưa mô hình kiểm soát của sản phẩm **về gần đúng mức KiotViet và Sapo đang làm**. Điểm khác biệt còn lại so với hai đối thủ đó là: phân quyền chi tiết hơn (6 quyền thay vì 2), có trường lý do lệch, và **giữ nguyên nhóm snapshot/cut-off YC-11→YC-15** — nhóm mà cả ba đối thủ đều không có tài liệu nào đề cập [RC-1][RC-12][RC-22].

**Vẫn còn treo:** Test 1 (snapshot) và Test 3 (mã chưa đếm) trong `kich-ban-test-trong-san-pham.md` chưa chạy. Quyết định 3 hiện dựa trên một nguồn không xác nhận lại được khi kiểm chứng — nên chạy Test 3 để chắc chắn.

---

## 1. Phạm vi

### Trong phạm vi

- Kiểm kê hàng hóa **đang nằm vật lý trong kho / trong cửa hàng** (bao gồm hàng trên quầy bán và hàng trong kho phía sau của cùng một điểm bán).
- Độ sâu dữ liệu: **mức mã hàng** và **mức lô — hạn dùng**.
- Kiểm kê toàn bộ, kiểm kê một phần (theo ngành hàng, nhóm hàng, nhà cung cấp, danh sách mã chọn tay).
- Kiểm kê cho một cửa hàng, và kiểm kê song song nhiều cửa hàng trong cùng một chuỗi.
- Đếm bằng quét mã vạch, gõ tay, và nhập từ file Excel.
- Đối chiếu chênh lệch về **số lượng và giá trị tiền**, cân bằng kho, sinh điều chỉnh tồn, lưu trữ và báo cáo.

### Ngoài phạm vi

- **Hàng không nằm trong kho tại thời điểm đếm không được kiểm kê**: hàng đang đi đường, hàng gửi đại lý, hàng ký gửi tại kho đối tác, hàng đã đặt nhưng chưa xuất. Các loại hàng này không xuất hiện trong phiếu đếm và không tham gia tính chênh lệch.
- Kiểm kê tới **mức serial / IMEI**.
- Kiểm kê tới **mức biến thể size — màu**.
- Kiểm kê tới **mức vị trí kệ (bin) / tọa độ trong kho**.
- Quản lý sơ đồ kho, tối ưu vị trí lưu trữ, nghiệp vụ soạn hàng (picking) — thuộc WMS, không thuộc sản phẩm này.

---

## 2. Các nhóm người dùng

| Vai trò | Cần gì từ nghiệp vụ này |
|---|---|
| **Chủ shop / chủ chuỗi** | Biết thực sự còn bao nhiêu tiền đang nằm trong kho, phát hiện thất thoát sớm, và thấy tỷ lệ chính xác tồn kho cải thiện qua từng kỳ. |
| **Quản lý cửa hàng** | Khởi tạo và điều phối đợt kiểm kê, kiểm soát ai được phép cân bằng kho thông qua phân quyền, và biết cửa hàng nào / người nào hay lệch. |
| **Nhân viên kho (thủ kho)** | Biết trước lịch kiểm kê để chuẩn bị, đếm nhanh, và có bằng chứng chứng minh mình đã đếm đúng khi bị quy trách nhiệm. |
| **Nhân viên đếm (kể cả thời vụ)** | Một màn hình đếm đơn giản tới mức không cần đào tạo: quét mã, gõ số, tiếp tục; và nhìn thấy tiến độ còn bao nhiêu chưa đếm. |
| **Thu ngân** | Tiếp tục bán hàng bình thường trong lúc kiểm kê diễn ra, không bị khóa POS và không phải ghi chép tay. |
| **Kế toán** | Bảng chênh lệch quy ra giá trị tiền, phiếu điều chỉnh sinh tự động từ kết quả kiểm kê, và không phải gõ lại bất kỳ con số nào. |
| **Kiểm toán viên / người kiểm tra nội bộ** | Tự tra cứu được biên bản kiểm kê đã xử lý, không sửa được, kèm dấu vết ai sửa số gì lúc nào. |

---

## 3. Yêu cầu theo tám bước xương sống

Mức ưu tiên: **Bắt buộc v1** — không có thì tính năng không dùng được hoặc cho ra số sai · **Nên có** — làm tăng đáng kể giá trị nhưng có thể ra sau · **Nâng cao** — thuộc các phiên bản sau.

**Phân bổ v2: 70 yêu cầu — 43 Bắt buộc v1 · 19 Nên có · 8 Nâng cao.** (v1 có 73 yêu cầu; ba mã YC-53, YC-54, YC-55 đã bị rút theo quyết định số 2.)

> ⚠️ **43 yêu cầu Bắt buộc v1 vẫn là nhiều cho một nghiệp vụ hoàn toàn mới**, và khảo sát cho thấy KiotViet lẫn Sapo ship nghiệp vụ này với luồng mỏng hơn hẳn. Con số này chưa được rà soát để siết lại — đây là việc nên làm trước khi viết mô tả chức năng, không phải sau.

### Bước 1 — Lập kế hoạch & phạm vi

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-01** | Quản lý cửa hàng cần tạo được một đợt kiểm kê mới, khai báo cửa hàng/kho được kiểm, mục đích và thời gian dự kiến, để cả đội biết đợt kiểm kê tồn tại trước khi bắt đầu đếm. | **Bắt buộc v1** |
| **YC-02** | Người tạo đợt cần chọn được phạm vi hàng hóa cần đếm theo nhiều cách: toàn bộ kho, theo ngành hàng / nhóm hàng, theo nhà cung cấp, hoặc theo một danh sách mã chọn tay. <br>*Vì sao: bắt đếm 20.000 mã trong một phiếu duy nhất là lý do khiến cửa hàng không bao giờ kiểm kê.* | **Bắt buộc v1** |
| **YC-03** | Hệ thống cần ngăn người dùng tạo một đợt kiểm kê mới có phạm vi hàng hóa chồng lấn với một đợt đang dở chưa chốt, trên cùng một kho. <br>*Vì sao: hai đợt chồng lấn cùng một mã sẽ điều chỉnh tồn hai lần cho cùng một chênh lệch.* | **Bắt buộc v1** |
| **YC-04** | Người tạo đợt cần chia được một đợt kiểm kê lớn thành nhiều phiếu đếm con giao cho từng người, và hệ thống gộp kết quả các phiếu con lên phiếu tổng. | **Nên có** |
| **YC-05** | Thủ kho cần xem được và in được danh sách mã hàng thuộc phạm vi trước ngày đếm, để chuẩn bị sắp xếp hàng và chia người. | **Nên có** |
| **YC-06** | **Phiếu ở trạng thái Chưa xử lý (lưu nháp) được xóa cứng** — xóa là mất hẳn khỏi hệ thống, không giữ lại bản ghi. <br>**Phiếu đã cân bằng kho (Đã xử lý) KHÔNG được hủy và KHÔNG được xóa**, trong mọi trường hợp; muốn đảo ngược tác động phải tạo chứng từ điều chỉnh mới (xem YC-60). <br>*Quyết định sản phẩm 2026-09-21. Hệ quả: không tồn tại trạng thái "đã hủy" — phiếu chỉ có hai trạng thái.* | **Bắt buộc v1** |
| **YC-07** | Chủ chuỗi cần khởi tạo và theo dõi được nhiều đợt kiểm kê ở nhiều cửa hàng cùng lúc, mỗi cửa hàng có tiến độ và người phụ trách riêng. | **Nên có** |
| **YC-08** | Hệ thống cần cho phép cấu hình bật/tắt từng bước của quy trình theo từng kho, để cửa hàng nhỏ chạy quy trình rút gọn còn chuỗi lớn chạy quy trình đầy đủ. | **Nên có** |
| **YC-09** | Người dùng cần chọn được một bộ cấu hình mặc định có sẵn khi tạo đợt (ví dụ: gói kiểm kê nhanh cho cửa hàng, gói đóng sổ cuối kỳ chạy đầy đủ các bước), thay vì phải khai báo lại từng tham số. | **Nâng cao** |
| **YC-10** | Hệ thống cần tự sinh lịch kiểm kê định kỳ và nhắc đến hạn, thay vì chỉ cho tạo tay khi cần. | **Nâng cao** |

### Bước 2 — Chốt snapshot / cut-off

> Đây là nhóm yêu cầu quan trọng nhất của toàn bộ nghiệp vụ. Nếu snapshot sai, mọi con số chênh lệch đều sai, nhưng người dùng vẫn tin và ra quyết định theo nó.

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-11** | Khi bắt đầu một đợt kiểm kê, hệ thống cần chốt lại tồn hệ thống của toàn bộ mã hàng trong phạm vi tại đúng thời điểm đó và giữ nguyên con số này suốt đợt, để chênh lệch luôn được so với một mốc cố định. <br>*Vì sao: kiểm kê kéo dài ba ngày mà mỗi ngày so với một số tồn khác nhau thì kết quả vô nghĩa.* | **Bắt buộc v1** |
| **YC-12** | Cửa hàng cần tiếp tục bán hàng bình thường trên POS trong suốt thời gian kiểm kê; hệ thống không được khóa việc bán hàng để phục vụ đếm. | **Bắt buộc v1** |
| **YC-13** | Hệ thống cần ghi nhận riêng mọi giao dịch làm thay đổi tồn phát sinh trong khoảng từ lúc chốt snapshot đến lúc kết thúc đếm (bán tại POS, nhập hàng, trả hàng, chuyển kho nội bộ, hủy hàng) và quy chiếu chúng khi tính chênh lệch, để số đếm thực tế được so đúng với mốc gốc. <br>*Vì sao: một đơn xuất phát sinh giữa chừng tạo ra chênh lệch giả, khiến thủ kho bị quy trách nhiệm oan.* | **Bắt buộc v1** |
| **YC-14** | Người cân bằng kho cần xem được danh sách các giao dịch phát sinh trong lúc đếm đã được tính vào điều chỉnh, để hiểu vì sao con số cuối cùng khác con số nhân viên đã đếm. | **Bắt buộc v1** |
| **YC-15** | Người tạo đợt cần thấy rõ thời điểm cut-off đã chốt (ngày giờ cụ thể) hiển thị trên phiếu và trên mọi báo cáo sinh ra từ đợt đó. | **Bắt buộc v1** |
| **YC-16** | Quản lý cần tùy chọn tạm dừng nhập/xuất kho thủ công (nhập hàng, chuyển kho) trong thời gian đếm, trong khi vẫn cho bán tại quầy. | **Nên có** |
| **YC-17** | Hệ thống cần cảnh báo và tự động xử lý một phiếu kiểm kê bị treo quá lâu sau thời điểm cut-off, vì snapshot càng cũ thì kết quả càng mất giá trị. | **Nên có** |

### Bước 3 — Đếm

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-18** | Nhân viên đếm cần nhập số đếm bằng cách quét mã vạch rồi gõ số lượng, trên một màn hình đơn giản tới mức không cần đào tạo. | **Bắt buộc v1** |
| **YC-19** | Nhân viên đếm cần nhập được số đếm bằng tay khi mã vạch bị mờ, bị rách hoặc sản phẩm không có mã. | **Bắt buộc v1** |
| **YC-20** | Kế toán / quản lý cần nhập kết quả đếm từ file Excel, vì nhiều cửa hàng vẫn đếm trên giấy rồi nhập lại một lần. <br>*Vì sao: đếm giấy rồi import là luồng chính ở một tỷ lệ khách hàng đáng kể, không phải trường hợp ngoại lệ.* | **Bắt buộc v1** |
| **YC-21** | Khi nhập từ Excel, người dùng cần xem trước kết quả và các dòng lỗi trước khi xác nhận ghi vào phiếu. <br>*Vì sao: file sai cột ghi đè sạch dữ liệu đã đếm cả buổi.* | **Bắt buộc v1** |
| **YC-22** | Với hàng có quản lý lô — hạn dùng, nhân viên đếm cần nhập số đếm tách theo từng lô, không chỉ tổng theo mã hàng. <br>*Vì sao: tổng theo mã có thể khớp trong khi từng lô lệch nhau, và lô sai làm sai toàn bộ cảnh báo hạn dùng.* | **Bắt buộc v1** |
| **YC-23** | Nhân viên đếm cần ghi nhận được hạn dùng thực tế đọc trên bao bì khi nó khác với hạn dùng hệ thống đang lưu. | **Nên có** |
| **YC-24** | Nhân viên đếm cần đánh dấu được hàng cận date, hết date, hàng hỏng ngay trong lượt đếm, để tận dụng một lần đi kho làm được hai việc. | **Nên có** |
| **YC-25** | Khi một mã được quét nhiều lần trong cùng phiếu, hệ thống cần cộng dồn hoặc cảnh báo trùng theo lựa chọn của người dùng, chứ không âm thầm ghi đè. <br>*Vì sao: đếm trùng một kệ hai lần là lỗi phổ biến nhất trong các đợt kiểm kê đông người.* | **Bắt buộc v1** |
| **YC-26** | Nhân viên đếm cần chọn được đơn vị tính khi nhập (thùng / lốc / lon) và hệ thống tự quy đổi về đơn vị tồn kho chuẩn. <br>*Vì sao: đếm thùng nhưng nhập vào ô số lượng lon tạo ra chênh lệch hàng chục lần.* | **Bắt buộc v1** |
| **YC-27** | Nhân viên đếm cần ghi nhận được mã hàng quét ra không có trong hệ thống hoặc không thuộc phạm vi đợt, thành một danh sách riêng để xử lý sau, thay vì bị chặn không nhập được. | **Bắt buộc v1** |
| **YC-28** | Mỗi dòng đếm cần cho phép ghi chú và đính kèm ảnh chụp để mô tả bất thường. <br>*Vì sao: mã vạch dán nhầm sản phẩm chỉ có thể giải thích bằng ảnh, không giải thích được bằng con số.* | **Nên có** |
| **YC-29** | Nhân viên đếm cần nhìn thấy tiến độ của phiếu: đã đếm bao nhiêu mã, còn bao nhiêu mã chưa đếm, để biết khi nào xong. | **Bắt buộc v1** |
| **YC-30** | Số đã nhập cần được lưu nháp liên tục và không mất khi thoát màn hình, đóng trình duyệt hoặc rớt kết nối tạm thời. | **Bắt buộc v1** |
| **YC-31** | Nhân viên đếm cần dùng được màn hình đếm trên điện thoại (web responsive, dùng camera quét mã) mà không cần cài ứng dụng riêng. | **Nên có** |
| **YC-32** | Nhiều người cần đếm song song trên cùng một đợt kiểm kê, mỗi người một phần phạm vi, và hệ thống gộp kết quả mà không đè lên nhau. | **Nên có** |
| **YC-33** | Màn hình đếm **hiển thị số tồn hệ thống ngay cạnh ô nhập số thực tế**, kèm chênh lệch tính tự động — giống cách các sản phẩm trên thị trường đang làm. <br>*Quyết định sản phẩm 2026-09-21: **không** làm đếm mù ở phiên bản này. Khảo sát cho thấy không đối thủ nào có đếm mù [RC-1][RC-12]; BA chọn đi theo thông lệ thị trường.* | **Bắt buộc v1** |
| **YC-34** | Hai người đếm độc lập cùng một phạm vi và hệ thống chỉ báo những mã hai người ra số khác nhau, dùng cho hàng giá trị cao. | **Nâng cao** |
| **YC-35** | Nhân viên đếm tiếp tục nhập được số khi mất kết nối mạng, và dữ liệu tự đồng bộ khi có mạng trở lại. | **Nâng cao** |
| **YC-36** | Hệ thống cần nhận được kết quả đếm từ thiết bị bên ngoài (máy kiểm kho chuyên dụng, RFID, cân đếm) qua một đường nhập liệu chuẩn. | **Nâng cao** |

### Bước 4 — Đối chiếu chênh lệch

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-37** | Người dùng cần xem một bảng đối chiếu đặt cạnh nhau: tồn hệ thống tại snapshot, số thực đếm, chênh lệch số lượng — cho toàn bộ mã trong phạm vi. <br>*Đây là hạt nhân của toàn bộ tính năng; nếu chỉ được giữ một màn hình thì giữ màn hình này.* | **Bắt buộc v1** |
| **YC-38** | Bảng chênh lệch cần quy chênh lệch ra **giá trị tiền** cho từng dòng và tổng cộng theo hướng thừa / thiếu, vì người ra quyết định nhìn tiền chứ không nhìn số lượng. | **Bắt buộc v1** |
| **YC-39** | Người dùng cần lọc và sắp xếp bảng chênh lệch theo giá trị lệch, tỷ lệ lệch, nhóm hàng và trạng thái dòng, để xử lý các dòng lớn trước. | **Bắt buộc v1** |
| **YC-40** | Hệ thống cần hiển thị rõ những mã thuộc phạm vi nhưng **chưa được đếm dòng nào**, tách khỏi các mã đã đếm ra 0. <br>*Vì sao: chưa đếm và đếm ra 0 là hai chuyện hoàn toàn khác nhau nhưng trông giống hệt nhau trên báo cáo.* | **Bắt buộc v1** |
| **YC-41** | Khi người dùng bấm cân bằng kho trong lúc còn mã chưa đếm, hệ thống **hiện thông báo nêu rõ số mã chưa đếm và cho người dùng chọn**: *bỏ qua các mã đó và cân bằng* (tồn của chúng giữ nguyên) hoặc *quay lại tiếp tục đếm*. Không được âm thầm quyết hộ, và **không được mặc định đưa mã chưa đếm về 0**. <br>*Quyết định sản phẩm 2026-09-21: đi theo mô hình Sapo [RC-16].* | **Bắt buộc v1** |
| **YC-42** | Với hàng có lô, bảng chênh lệch cần thể hiện được cả trường hợp tổng theo mã hàng khớp nhưng phân bổ giữa các lô bị lệch. | **Bắt buộc v1** |
| **YC-43** | **Mỗi dòng đếm có một trường lý do lệch**, chọn từ danh mục có sẵn (nhập liệu sai, hàng hỏng/hủy, mất hàng, sai đơn vị, bán không ghi nhận, khác). <br>*Vì sao: phần lớn chênh lệch đến từ sai sót nhập liệu chứ không phải mất hàng; không phân loại thì không sửa được nguyên nhân gốc. Trong ba đối thủ chỉ CukCuk có trường này [RC-22].* <br>*Quyết định sản phẩm 2026-09-21: nâng từ Nên có lên Bắt buộc v1.* | **Bắt buộc v1** |
| **YC-44** | Người dùng cần xuất bảng chênh lệch ra Excel để xử lý và đối chiếu ngoài hệ thống. | **Nên có** |
| **YC-45** | Mỗi chênh lệch vượt ngưỡng cần mở được một case điều tra có người chịu trách nhiệm và hạn xử lý, theo dõi độc lập sau khi đợt kiểm kê đã đóng. | **Nâng cao** |

### Bước 5 — Đếm lại có điều kiện

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-46** | Quản lý cần cấu hình ngưỡng lệch (theo tỷ lệ phần trăm và theo giá trị tiền) làm mốc chung cho hai việc: **kích hoạt đếm lại**, và **cảnh báo trên màn hình xác nhận trước khi cân bằng kho**. | **Bắt buộc v1** |
| **YC-47** | Hệ thống cần tự đánh dấu những dòng vượt ngưỡng lệch là cần đếm lại, để đội đếm chỉ phải quay lại đúng những mã đó thay vì đếm lại toàn kho. | **Nên có** |
| **YC-48** | Thủ kho cần chủ động yêu cầu đếm lại một mã hoặc một nhóm mã khi thấy kết quả bất hợp lý, kèm lý do. <br>*Vì sao: thủ kho sợ bị quy trách nhiệm oan; quyền yêu cầu đếm lại là thứ khiến họ chấp nhận quy trình.* | **Nên có** |
| **YC-49** | Kết quả các vòng đếm phải được lưu tách bạch (vòng 1, vòng 2, ...) và người cân bằng kho xem được số của từng vòng, chứ không chỉ thấy con số cuối cùng. | **Bắt buộc v1** |

### Bước 6 — Phân quyền & xác nhận trước khi cân bằng kho

> **Quyết định sản phẩm 2026-09-21: nghiệp vụ này KHÔNG có bước duyệt phiếu.** Chốt kiểm soát duy nhất là **quyền cân bằng kho**. Ba yêu cầu về luồng duyệt trong v1 (YC-53, YC-54, YC-55) đã bị loại bỏ — xem mục 5.

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-50** | Phiếu ở trạng thái **Chưa xử lý** (mới lưu nháp) không tác động gì tới tồn kho. Tồn kho chỉ thay đổi khi người dùng chủ động bấm **cân bằng kho**, và phiếu chuyển sang **Đã xử lý**. <br>*Hai trạng thái này là toàn bộ vòng đời phiếu — quyết định sản phẩm 2026-09-21.* | **Bắt buộc v1** |
| **YC-51** | Hệ thống tách **sáu quyền độc lập**, gán được riêng cho từng vai trò: **tạo phiếu · xem phiếu · sửa phiếu · cân bằng kho · in phiếu · nhập từ Excel**. <br>*Vì sao: vì không có bước duyệt, quyền **cân bằng kho** là chốt kiểm soát thất thoát duy nhất — người đếm có thể được cấp quyền tạo và sửa phiếu mà không có quyền cân bằng kho. Đối thủ chỉ có hai quyền, nên ai tạo được phiếu cũng cân bằng được kho [RC-12][RC-13].* | **Bắt buộc v1** |
| **YC-52** | Trước khi cân bằng kho, hệ thống hiển thị **tóm tắt tác động** và yêu cầu xác nhận: tổng giá trị tăng, tổng giá trị giảm, số dòng bị ảnh hưởng, số mã chưa đếm. <br>*Vì sao: cân bằng nhầm một phiếu sai làm hỏng số tồn của cả cửa hàng và rất khó lần ngược. Vì không có bước duyệt, màn hình xác nhận này là lớp chặn cuối cùng.* | **Bắt buộc v1** |

### Bước 7 — Điều chỉnh tồn & hạch toán

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-56** | Khi người dùng bấm cân bằng kho, hệ thống cần tự sinh chứng từ điều chỉnh tăng/giảm tồn kho và cập nhật tồn, mà không ai phải nhập lại số bằng tay. <br>*Vì sao: gửi kết quả cho kế toán tự gõ lại là nguồn sai số lớn nhất và là việc khách hàng ghét nhất.* | **Bắt buộc v1** |
| **YC-57** | Chứng từ điều chỉnh sinh ra phải truy ngược được về đúng đợt kiểm kê và đúng dòng đếm đã tạo ra nó. | **Bắt buộc v1** |
| **YC-58** | Việc điều chỉnh phải cập nhật tồn ở **mức lô** cho hàng có quản lý lô, chứ không chỉ cộng trừ tổng theo mã hàng. | **Bắt buộc v1** |
| **YC-59** | Hệ thống cần áp một quy tắc giá rõ ràng và nhất quán cho phần hàng thừa/thiếu khi ghi nhận giá trị điều chỉnh, và hiển thị giá đã áp trên chứng từ. <br>*Vì sao: điều chỉnh số lượng mà không quyết định giá vốn khiến giá trị tồn kho sai lệch âm thầm.* | **Bắt buộc v1** |
| **YC-60** | Sau khi phiếu chuyển sang **Đã xử lý**, không ai được sửa trực tiếp số liệu trên phiếu — kể cả người có quyền sửa phiếu; muốn thay đổi phải tạo một chứng từ điều chỉnh mới. | **Bắt buộc v1** |
| **YC-61** | Mọi thay đổi tồn kho sinh ra từ nghiệp vụ này phải gắn với một chứng từ có loại, có người thực hiện và có lý do — không tồn tại đường sửa tồn tự do. | **Bắt buộc v1** |
| **YC-62** | Kế toán cần chứng từ điều chỉnh mang thông tin định khoản phù hợp cho phần thừa chờ xử lý và thiếu chờ xử lý, để không phải hạch toán lại thủ công. | **Nên có** |
| **YC-63** | Với chuỗi nhiều cửa hàng, việc điều chỉnh phải ghi vào đúng kho của cửa hàng được kiểm, không ảnh hưởng tồn của cửa hàng khác. | **Bắt buộc v1** |

### Bước 8 — Lưu trữ & báo cáo

| ID | Yêu cầu | Ưu tiên |
|---|---|---|
| **YC-64** | Hệ thống cần lưu vĩnh viễn toàn bộ dữ liệu của **mọi phiếu đã cân bằng kho (Đã xử lý)** ở **mức từng dòng đếm**, không chỉ mức tổng, và **không cho xóa dưới bất kỳ hình thức nào**. <br>*Phạm vi này chỉ áp cho phiếu Đã xử lý. Phiếu Chưa xử lý bị xóa cứng theo YC-06 và không để lại dữ liệu.* | **Bắt buộc v1** |
| **YC-65** | Hệ thống cần ghi nhật ký thay đổi (audit trail): ai nhập hay sửa số nào, lúc nào, từ giá trị bao nhiêu thành bao nhiêu, và ai chuyển trạng thái phiếu. | **Bắt buộc v1** |
| **YC-66** | Người dùng cần in và xuất được biên bản kiểm kê ra PDF với đầy đủ thông tin các bên tham gia, phục vụ lưu hồ sơ và kiểm toán; biên bản của phiếu Đã xử lý không sửa được. Thao tác in gắn với quyền **in phiếu**. | **Bắt buộc v1** |
| **YC-67** | Người dùng cần tra cứu lại lịch sử các đợt kiểm kê đã thực hiện theo cửa hàng, theo kỳ và theo người thực hiện. | **Bắt buộc v1** |
| **YC-68** | Chủ shop cần một báo cáo tỷ lệ chính xác tồn kho theo kỳ, theo cửa hàng và theo người đếm, để thấy chất lượng quản lý kho cải thiện hay xấu đi. <br>*Vì sao: giá trị người mua thực sự tìm kiếm là sự yên tâm theo thời gian, không phải một con số chênh lệch của một lần.* | **Nên có** |
| **YC-69** | Người dùng cần báo cáo so sánh giữa các kỳ kiểm kê để phát hiện mã hàng, nhóm hàng hoặc cửa hàng lệch lặp đi lặp lại. | **Nên có** |
| **YC-70** | Người dùng cần báo cáo kết quả kiểm kê phân tích theo lý do lệch, để biết bao nhiêu phần trăm chênh lệch đến từ nhập liệu sai và bao nhiêu từ mất hàng. | **Nên có** |
| **YC-71** | Chủ chuỗi cần một màn hình tổng hợp kết quả kiểm kê của tất cả cửa hàng trong chuỗi trong cùng một kỳ. | **Nên có** |
| **YC-72** | Hệ thống cần hiển thị độ tin cậy của tồn từng mã dựa trên lịch sử lệch, để gợi ý mã nào cần được kiểm thường xuyên hơn. | **Nâng cao** |
| **YC-73** | Hệ thống cần tự sinh danh sách mã cần đếm mỗi ngày theo giá trị và lịch sử lệch (kiểm kê luân phiên), để cửa hàng phủ hết kho trong năm mà không bao giờ phải dừng bán. | **Nâng cao** |

---

## 4. Quy tắc nghiệp vụ cần chốt trước khi viết mô tả chức năng

Các điểm dưới đây chưa có lời giải trong quá trình brainstorm và phải được trả lời trước khi đặc tả, vì mỗi lựa chọn kéo theo mô hình dữ liệu và hành vi khác nhau.

1. ~~**Mã thuộc phạm vi nhưng không được đếm dòng nào thì xử lý ra sao khi chốt phiếu?**~~ — ✅ **ĐÃ CHỐT 2026-09-21.**
   Hệ thống **hiện thông báo** nêu rõ số mã chưa đếm và cho người dùng chọn: *bỏ qua và cân bằng* (tồn của các mã đó **giữ nguyên**) hoặc *quay lại tiếp tục đếm*. **Không bao giờ mặc định đưa về 0.** Đi theo mô hình Sapo [RC-16].
   *Đã phản ánh vào YC-40, YC-41.*

2. **Giá nào được áp cho phần hàng thừa và hàng thiếu khi ghi nhận giá trị điều chỉnh?**
   (a) Giá vốn bình quân hiện hành tại thời điểm chốt · (b) Giá vốn tại thời điểm snapshot · (c) Giá nhập gần nhất · (d) Giá của đúng lô được điều chỉnh (với hàng có lô).
   *Ảnh hưởng trực tiếp YC-38, YC-59.*

3. **Danh sách chính xác các loại giao dịch nào được tính vào tồn hệ thống tại thời điểm T, và các giao dịch phát sinh trong lúc đếm được quy chiếu theo nguyên tắc nào?**
   Cần chốt từng loại: bán tại POS, trả hàng từ khách, nhập hàng từ nhà cung cấp, trả hàng cho nhà cung cấp, chuyển kho nội bộ (bên gửi / bên nhận), hủy hàng, hàng khuyến mãi/quà tặng xuất kho. Với mỗi loại: tính vào snapshot theo thời điểm tạo chứng từ hay thời điểm chứng từ được ghi sổ?
   *Ảnh hưởng trực tiếp YC-11, YC-13.*

4. **Ngưỡng lệch được định nghĩa thế nào và ở cấp nào?**
   (a) Một ngưỡng chung toàn hệ thống · (b) Theo từng kho/cửa hàng · (c) Theo nhóm hàng · (d) Kết hợp cả tỷ lệ phần trăm và giá trị tuyệt đối, và khi nào áp điều kiện "hoặc" / "và".
   *Ảnh hưởng YC-46, YC-47, YC-55.*

5. **Một người có được đếm chính kho mà mình đang trực tiếp giữ hay không?**
   (a) Cho phép, nhưng không cấp quyền **cân bằng kho** cho người đó · (b) Cấm hoàn toàn · (c) Cho phép không ràng buộc gì.
   *Ảnh hưởng YC-51. Lưu ý: vì đã bỏ bước duyệt, phương án (a) chỉ có tác dụng nếu quyền cân bằng kho thực sự được giao cho người khác — nếu cùng một người có cả hai quyền thì kiểm kê mất tác dụng kiểm soát thất thoát.*

6. ~~**Danh sách trạng thái của phiếu kiểm kê và ai được phép chuyển trạng thái nào?**~~ — ✅ **ĐÃ CHỐT 2026-09-21.**
   Phiếu có đúng **hai trạng thái**: **Chưa xử lý** (mới lưu nháp, chưa tác động tồn kho) → **Đã xử lý** (đã cân bằng tồn kho). Không có trạng thái chờ duyệt, và **không có trạng thái "đã hủy"**: phiếu Chưa xử lý thì xóa cứng, phiếu Đã xử lý thì không hủy được.
   *Đã phản ánh vào YC-06, YC-50, YC-51, YC-60, YC-64.*

7. **Phiếu kiểm kê treo quá bao lâu kể từ cut-off thì bị coi là hết hiệu lực, và khi đó hệ thống làm gì?**
   (a) Tự hủy · (b) Chỉ cảnh báo, vẫn cho chốt · (c) Chặn chốt, bắt tạo đợt mới với snapshot mới.
   *Ảnh hưởng YC-17.*

8. **Mã hàng lạ quét ra trong lúc đếm (không có trong hệ thống) được xử lý thế nào sau đợt kiểm kê?**
   (a) Chỉ ghi nhận thành danh sách để người dùng tự xử lý · (b) Cho phép tạo mã hàng mới ngay từ đợt kiểm kê và ghi nhận tồn · (c) Bắt buộc bỏ qua, không đưa vào điều chỉnh.
   *Ảnh hưởng YC-27.*

9. **Với hàng có lô: nếu tổng theo mã hàng khớp nhưng phân bổ giữa các lô lệch, hệ thống sinh điều chỉnh thế nào?**
   (a) Một cặp điều chỉnh tăng lô này / giảm lô kia, giá trị tiền bằng 0 · (b) Hai chứng từ độc lập · (c) Yêu cầu người cân bằng kho xác nhận riêng cho nhóm này.
   *Ảnh hưởng YC-42, YC-58.*

10. **Hàng đã có mặt vật lý trong kho nhưng chưa được ghi nhận nhập kho trên hệ thống (ví dụ hàng khách trả đang chờ xử lý, hàng nhà cung cấp mới giao chưa lên phiếu) được đếm hay bị loại trừ?**
    (a) Đếm và để lộ ra thành chênh lệch thừa · (b) Loại trừ bằng cách đánh dấu trạng thái hàng · (c) Yêu cầu hoàn tất chứng từ nhập trước khi chốt snapshot.

---

## 5. Ngoài phạm vi lần này

Các hướng đã được cân nhắc trong quá trình brainstorm và chủ động cắt bỏ khỏi bản này, ghi lại để không bị mất:

- **Kiểm kê tới mức serial/IMEI, size-màu, vị trí kệ (bin)** — loại bỏ hoàn toàn theo quyết định phạm vi về độ sâu dữ liệu.
- **Kiểm kê hàng không nằm trong kho** (đi đường, gửi đại lý, ký gửi tại kho đối tác, đã đặt chưa xuất) — loại bỏ hoàn toàn.
- **Đếm mù** — ❌ **loại bỏ theo quyết định sản phẩm 2026-09-21.** Màn hình đếm sẽ hiển thị tồn hệ thống như các đối thủ (xem YC-33). Ghi lại để không mất: khảo sát cho thấy **không đối thủ nào có đếm mù** [RC-1][RC-12], nên đây từng là một khoảng trống cạnh tranh; nếu sau này phát sinh nhu cầu chống gian lận nội bộ, đây là chỗ quay lại.
- **Luồng duyệt phiếu kiểm kê** (YC-53 từ chối phiếu, YC-54 duyệt từng dòng, YC-55 duyệt nhiều cấp) — ❌ **loại bỏ theo quyết định sản phẩm 2026-09-21.** Thay bằng phân quyền sáu quyền (YC-51) và màn hình xác nhận tác động (YC-52). Ba mã YC-53, YC-54, YC-55 **được rút khỏi tài liệu và không tái sử dụng** cho yêu cầu khác.
- **Liên thông CSDL Dược quốc gia / nghiệp vụ nhà thuốc** — ❌ **không thuộc phase này** theo quyết định 2026-09-21. Ghi lại để không mất: KiotViet tự động đồng bộ phiếu kiểm kho đã cân bằng lên CSDL Dược và **cấm tạo lô mới khi kiểm kê** [RC-6]; Sapo thì không đưa kiểm kho vào phạm vi đồng bộ [RC-17]. Nếu phase sau nhắm khách hàng nhà thuốc, ràng buộc này **xung đột trực tiếp với YC-27** (ghi nhận mã/lô lạ phát sinh khi đếm) và phải giải quyết trước khi đặc tả.
- **Đếm hai người độc lập đối chiếu** (YC-34) — v2 trở đi, gắn với phân khúc hàng giá trị cao.
- **Kiểm kê luân phiên tự sinh danh sách hằng ngày (cycle counting)** (YC-73) — cần được mô hình hóa như một chế độ kiểm kê ngang hàng với kiểm kê toàn bộ ngay từ khâu thiết kế dữ liệu, dù chỉ triển khai sau.
- **Ứng dụng di động chạy offline có hàng đợi đồng bộ** (YC-35) — v1 chỉ dùng web responsive mở trên điện thoại kèm camera quét mã.
- **Nhận kết quả đếm từ RFID / cân đếm / thiết bị kiểm kho ngoài** (YC-36).
- **Case điều tra chênh lệch có người chịu trách nhiệm và hạn xử lý** (YC-45).
- **Chỉ số độ tin cậy tồn theo từng mã** (YC-72).
- **Bộ cấu hình mặc định theo phân khúc khách hàng** (YC-09) — ba gói (chống thất thoát hàng giá trị cao / kiểm kê luân phiên cho cửa hàng / đóng sổ kiểm toán) nên là ba bộ cấu hình của cùng một nghiệp vụ, không phải ba module riêng.
- **Lấy mẫu thay cho đếm toàn bộ** với nhóm hàng giá trị thấp — chưa đủ cơ sở nghiệp vụ để đặc tả ở bản này.

---

> **Ký hiệu `[RC-n]`** trỏ tới nguồn số *n* trong phụ lục nguồn của báo cáo khảo sát đối thủ: `docs/research/competitive-kiem-ke-kho-sapo-kiotviet-cukcuk-2026-09-21/research.md`, mục 9.
