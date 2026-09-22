---
id: SPEC-kiem-ke-kho
companions:
  - ../../brainstorming/brainstorm-kiem-ke-kho-2026-09-21/yeu-cau-nguoi-dung-kiem-ke-kho.md
  - quy-tac-nghiep-vu-can-chot.md
sources:
  - ../../research/competitive-kiem-ke-kho-sapo-kiotviet-cukcuk-2026-09-21/research.md
---

> **Canonical contract.** SPEC này cùng các file trong `companions:` là hợp đồng đầy đủ về cái cần xây, cần kiểm thử và cần nghiệm thu. Tài liệu trong `sources:` chỉ dùng để truy vết lý do.

# Kiểm kê kho cho phần mềm POS bán hàng

## Why

Phần mềm POS hiện **chưa có nghiệp vụ kiểm kê kho**, nên cửa hàng không có cách nào hợp lệ để đối chiếu tồn hệ thống với tồn thực tế: họ đếm tay, gõ lại vào Excel, rồi sửa tồn bằng những đường không để lại dấu vết. Hệ quả là số tồn trên hệ thống trôi dần khỏi sự thật, bán hàng bị hụt hoặc bán quá, kế toán không có căn cứ đóng sổ, và thất thoát chỉ lộ ra khi đã thành thói quen. Đây vừa là **một khoảng trống phải lấp** (chủ shop, quản lý cửa hàng, thủ kho, kế toán đều đang mắc), vừa là **một cơ hội**: khảo sát ba đối thủ trên thị trường Việt Nam cho thấy không sản phẩm nào có tài liệu đề cập tới việc chốt tồn tại một thời điểm, trong khi POS vẫn bán liên tục trong lúc đếm — nghĩa là con số chênh lệch của họ có thể sai một cách im lặng.

## Capabilities

> **Mã đã rút:** CAP-7, CAP-11, CAP-16 bị loại khỏi phạm vi ngày 2026-09-21. Ba mã này **không được tái sử dụng** cho capability khác; phần bị cắt nằm ở mục Non-goals.

- **CAP-1**
  - **intent:** Quản lý cửa hàng tạo được một đợt kiểm kê và chọn phạm vi hàng hóa cần đếm (toàn bộ kho, theo ngành hàng/nhóm hàng, theo nhà cung cấp, hoặc danh sách mã chọn tay), để không bao giờ phải đếm cả kho chỉ vì muốn kiểm một nhóm hàng.
  - **success:** Tạo được đợt với từng kiểu phạm vi trên; khi phạm vi chồng lấn với một đợt *Chưa xử lý* khác trên cùng kho, hệ thống chặn và nêu rõ đợt đang xung đột.

- **CAP-2**
  - **intent:** Hệ thống chốt tồn hệ thống của toàn bộ mã trong phạm vi tại đúng thời điểm mở đợt, dùng làm mốc tham chiếu của đợt: tiêu đề biên bản *"kiểm kê tại thời điểm T0"*, và cơ sở xử lý những mã **chưa được đếm dòng nào** (vì chúng không có mốc thời gian riêng).
  - **success:** Mở đợt, để một ngày, mở lại — cột tồn snapshot không đổi. Thời điểm cut-off (ngày giờ cụ thể) hiển thị trên phiếu và trên mọi báo cáo sinh từ đợt đó.
  - **lưu ý:** Snapshot **không** phải là cơ sở tính chênh lệch của dòng đã đếm — việc đó thuộc CAP-3.

- **CAP-3**
  - **intent:** Cửa hàng bán hàng bình thường suốt thời gian kiểm kê. Khi một dòng được đếm, hệ thống ghi **đồng thời** số thực đếm và **tồn hệ thống của đúng mã/lô đó tại đúng thời điểm ấy**; chênh lệch của dòng đóng băng ngay tại đó. Không tua ngược, không cộng trừ lại theo chứng từ.
  - **success:** Đếm mã A lúc 9h, bán một đơn có mã A lúc 11h, cân bằng kho lúc 15h — chênh lệch của mã A vẫn đúng bằng chênh lệch đo được lúc 9h và **không** bị đơn hàng 11h làm sai lệch. POS không bị chặn ở bất kỳ thời điểm nào. Mỗi dòng trên biên bản hiển thị được thời điểm đếm của chính nó.

- **CAP-4**
  - **intent:** Nhân viên đếm nhập được số thực tế bằng quét mã vạch hoặc gõ tay trên một màn hình đơn giản tới mức không cần đào tạo, có chọn đơn vị tính, có tiến độ, và số đã nhập không mất.
  - **success:** Người chưa từng dùng phần mềm đếm được 20 mã mà không cần hướng dẫn; đếm bằng thùng rồi hệ thống tự quy đổi về đơn vị tồn chuẩn; quét trùng một mã thì cộng dồn hoặc cảnh báo theo lựa chọn chứ không âm thầm ghi đè; thoát màn hình rồi quay lại, số đã nhập còn nguyên. **Mỗi dòng đếm mang thời điểm đếm của chính nó** — đây là dữ liệu CAP-3 dựa vào, không phải thông tin trang trí.

- **CAP-5**
  - **intent:** Kế toán hoặc quản lý nạp kết quả đếm từ file Excel, vì nhiều cửa hàng vẫn đếm trên giấy rồi nhập lại một lần.
  - **success:** Nạp file đúng định dạng thì số vào phiếu; nạp file sai cột hoặc sai mã thì hệ thống hiện bảng xem trước liệt kê dòng lỗi và **không** ghi gì vào phiếu cho tới khi người dùng xác nhận. Trước khi ghi, người dùng **khai được một thời điểm đếm cho cả lô import** (mặc định là thời điểm import, sửa được) — cửa hàng đếm trên giấy lúc 8h rồi nhập lúc 17h phải khai 8h, nếu không toàn bộ giao dịch bán trong ngày bị tính nhầm thành chênh lệch.

- **CAP-6**
  - **intent:** Với hàng có quản lý lô — hạn dùng, nhân viên đếm nhập số tách theo từng lô thay vì chỉ tổng theo mã hàng.
  - **success:** Một mã có ba lô, đếm lệch giữa các lô nhưng tổng khớp — hệ thống vẫn phát hiện và thể hiện được chênh lệch ở mức lô.

- **CAP-8**
  - **intent:** Người dùng xem được bảng đối chiếu đặt cạnh nhau — **tồn hệ thống tại thời điểm đếm dòng đó**, số thực đếm, chênh lệch số lượng và **chênh lệch quy ra tiền** — lọc và sắp xếp được để xử lý dòng lớn trước.
  - **success:** Bảng hiện đủ ba cột số cộng cột giá trị tiền cho từng dòng và tổng theo hướng thừa/thiếu; sắp xếp theo giá trị lệch đưa dòng đắt nhất lên đầu. Dòng **chưa đếm** hiển thị tồn snapshot của đợt thay vì tồn tại thời điểm đếm, và được đánh dấu rõ là chưa đếm (CAP-9).

- **CAP-9**
  - **intent:** Hệ thống phân biệt rõ mã **chưa được đếm dòng nào** với mã **đã đếm ra 0**, và khi người dùng cân bằng kho trong lúc còn mã chưa đếm thì bắt họ quyết định chứ không quyết hộ.
  - **success:** Phiếu 15 mã, đếm 5, bấm cân bằng — hệ thống nêu rõ 10 mã chưa đếm và cho chọn *bỏ qua và cân bằng* (tồn 10 mã đó giữ nguyên) hoặc *quay lại tiếp tục đếm*. Không có đường nào đưa mã chưa đếm về 0 một cách mặc định.

- **CAP-10**
  - **intent:** Người xử lý **tự nhập** lý do lệch cho từng dòng chênh lệch bằng văn bản tự do, để người đọc phiếu về sau hiểu được vì sao dòng đó lệch.
  - **success:** Mỗi dòng lệch nhận được một ô lý do nhập tay; nội dung đã nhập hiển thị trên bảng đối chiếu và trên biên bản xuất ra.

- **CAP-12**
  - **intent:** Quản trị gán được sáu quyền độc lập cho từng vai trò — tạo phiếu, xem phiếu, sửa phiếu, cân bằng kho, in phiếu, nhập từ Excel — để người đếm có thể nhập số mà không tự làm đổi được tồn kho.
  - **success:** Một tài khoản có quyền tạo và sửa phiếu nhưng không có quyền cân bằng kho: đếm và lưu được, nhưng không có đường nào làm thay đổi tồn kho thật.

- **CAP-13**
  - **intent:** Người có quyền cân bằng kho bấm cân bằng, xác nhận qua một popup đơn giản, và hệ thống sinh chứng từ điều chỉnh tăng/giảm cập nhật tồn — không ai phải gõ lại số.
  - **success:** Bấm cân bằng kho hiện đúng một popup hỏi có muốn cân bằng tồn kho không; huỷ thì không có gì thay đổi; xác nhận thì tồn kho đổi đúng và chứng từ điều chỉnh truy ngược được về đúng đợt và đúng dòng đếm. Với hàng có lô, điều chỉnh ghi ở mức lô; với chuỗi, chỉ kho của cửa hàng được kiểm bị ảnh hưởng.

- **CAP-14**
  - **intent:** Sau khi phiếu chuyển sang *Đã xử lý*, dữ liệu của nó bất biến và mọi thay đổi tồn sinh ra từ nghiệp vụ này đều gắn với một chứng từ có loại, có người và có lý do.
  - **success:** Không tồn tại thao tác nào sửa hay xóa được một phiếu *Đã xử lý*, kể cả với tài khoản có quyền sửa phiếu; nhật ký ghi được ai nhập hay sửa số nào, lúc nào, từ giá trị bao nhiêu thành bao nhiêu.

- **CAP-15**
  - **intent:** Người dùng in và xuất được biên bản kiểm kê ra PDF, và tra cứu lại lịch sử các đợt đã thực hiện theo cửa hàng, theo kỳ và theo người thực hiện.
  - **success:** Xuất được biên bản của một đợt *Đã xử lý* với đủ thông tin các bên tham gia, và biên bản đó không sửa được; tra cứu ra đúng đợt cần tìm theo cả ba tiêu chí.

## Constraints

- **POS vẫn tiếp tục bán hàng trong suốt thời gian kiểm kê.** Không được thiết kế theo giả định cửa hàng đóng cửa để đếm. Đây là ràng buộc bẻ toàn bộ kiến trúc: nó làm việc **chốt tồn tại thời điểm đếm từng dòng** (CAP-3) trở thành bắt buộc, không phải biện pháp phòng ngừa tùy chọn.
- **Độ sâu dữ liệu dừng ở mức mã hàng và mức lô — hạn dùng.** Mọi thiết kế không được giả định có serial, biến thể size–màu, hay vị trí kệ.
- **Chỉ hàng đang nằm vật lý trong kho/cửa hàng mới được kiểm kê.** Hàng đi đường, gửi đại lý, ký gửi, đã đặt chưa xuất không xuất hiện trên phiếu đếm và không tham gia tính chênh lệch.
- **Không có bước duyệt phiếu.** Chốt kiểm soát duy nhất là **quyền cân bằng kho** trong bộ sáu quyền (CAP-12). Không được thiết kế trạng thái chờ duyệt, luồng từ chối, hay duyệt nhiều cấp.
- **Phiếu có đúng hai trạng thái: *Chưa xử lý* → *Đã xử lý*.** Không có trạng thái thứ ba, kể cả "đã hủy".
- **Phiếu *Chưa xử lý* bị xóa cứng và không ghi log** — xóa là mất hẳn, không để lại bản ghi nào, kể cả bản ghi việc xóa. **Phiếu *Đã xử lý* không hủy được và không xóa được** trong mọi trường hợp; muốn đảo ngược tác động phải tạo chứng từ điều chỉnh mới.
- **Mọi bản ghi trong sổ chuyển động tồn kho chạm vào bộ ba `(kho, mã hàng, lô)` đều được tính, bất kể chứng từ nào sinh ra nó.** Không được hiện thực bằng một danh sách loại chứng từ liệt kê sẵn: loại chứng từ mới phát sinh về sau phải tự động đúng, không cần ai nhớ quay lại bổ sung.
- **Mốc thời gian dùng thời điểm chứng từ tác động vào sổ tồn**, không phải thời điểm tạo chứng từ. Snapshot đọc từ chính sổ đó, nên hai vế phải cùng một cơ sở thời gian thì mới khớp.
- **Chặn ghi lùi ngày vào khoảng thời gian có phiếu kiểm kê đang mở trên kho đó.** Chứng từ ghi lùi tạo ra chênh lệch giả mà không ai lần ngược ra được.
- **Hàng đang trên đường giữa hai kho không thuộc kho nào** cho tới khi bên nhận ghi nhận. Chuyển kho nội bộ chỉ tính ngay ở bên gửi. Nhất quán với ràng buộc chỉ kiểm hàng nằm vật lý trong kho.
- **Giá trị chênh lệch được tính theo giá vốn tại thời điểm cân bằng kho** — không phải giá vốn tại snapshot, không phải giá nhập gần nhất. Áp cho cả CAP-8 và CAP-13.
- **Màn hình đếm hiển thị tồn hệ thống ngay cạnh ô nhập.** Không làm đếm mù ở phiên bản này.
- **Mã chưa đếm không bao giờ được tự động quy về 0.** Hệ thống phải hỏi người dùng (CAP-9).
- **Mọi thay đổi tồn kho sinh ra từ nghiệp vụ này phải đi qua một chứng từ có loại, có người thực hiện và có lý do.** Không tồn tại đường sửa tồn tự do.
- **Sản phẩm là POS bán hàng, không phải WMS hay ERP.** Nghiệp vụ này tái sử dụng danh mục kho, cơ chế phân quyền, giá vốn và quản lý lô–HSD sẵn có, không dựng hệ thống song song.

## Non-goals

- Kiểm kê tới mức **serial / IMEI**, mức **biến thể size — màu**, hoặc mức **vị trí kệ (bin)**.
- Kiểm kê **hàng không nằm trong kho**: đi đường, gửi đại lý, ký gửi tại kho đối tác, đã đặt chưa xuất.
- **Luồng duyệt phiếu kiểm kê** — từ chối phiếu, duyệt từng dòng, duyệt nhiều cấp. Đã chủ động cắt, thay bằng phân quyền.
- **Đếm mù.** Đã chủ động cắt; ghi lại để biết đây từng được xác định là một khoảng trống cạnh tranh.
- **Ghi nhận mã hàng lạ / ngoài phạm vi quét ra trong lúc đếm.** Đã chủ động cắt (CAP-7 rút).
- **Đếm lại có điều kiện theo ngưỡng lệch**, kể cả khái niệm ngưỡng lệch và việc lưu tách bạch kết quả từng vòng đếm. Đã chủ động cắt (CAP-11 rút).
- **Báo cáo tỷ lệ chính xác tồn kho theo kỳ.** Đã chủ động cắt (CAP-16 rút). Ghi lại để biết: đây là chỉ số gắn với nhu cầu *yên tâm theo thời gian* của chủ shop, không phải chỉ số vận hành.
- **Liên thông CSDL Dược quốc gia và nghiệp vụ nhà thuốc** — không thuộc phase này.
- **Nghiệp vụ WMS**: quản lý sơ đồ kho, tối ưu vị trí lưu trữ, soạn hàng (picking).

## Success signal

Một cửa hàng 20.000 mã chạy kiểm kê toàn kho trong một buổi tối **trong khi POS vẫn bán bình thường**, và sáng hôm sau mở bán với số tồn tin được — không phải đối chiếu lại bằng Excel, không phải gõ lại số nào cho kế toán. Kiểm chứng bằng cách chạy một đợt thật có bán hàng xen giữa: chênh lệch cuối cùng giải thích được từng đồng, mọi phiếu đã xử lý đều bất biến và truy ngược được về từng dòng đếm.

## Assumptions

- Phần mềm POS đã có sẵn danh mục kho, cơ chế phân quyền, giá vốn, quản lý lô–hạn dùng và máy quét mã tại quầy; nghiệp vụ kiểm kê dùng lại chúng.
- Có sẵn giá vốn ở mức đủ tin cậy để quy chênh lệch ra giá trị tiền (CAP-8).
- Mô hình dữ liệu hiện tại cho phép một cửa hàng có một hoặc nhiều kho, và đợt kiểm kê gắn được vào đúng một kho.

## Open Questions

- Bốn quy tắc nghiệp vụ còn lại chưa chốt (`QT-5`, `QT-6`, `QT-8`, `QT-9`) — chi tiết và các phương án nằm trong `quy-tac-nghiep-vu-can-chot.md`.
- **Hành vi thực tế của đối thủ về snapshot và về mã chưa đếm chưa được xác nhận trực tiếp.** Quyết định trong CAP-9 dựa trên một nguồn tài liệu không tải lại được khi kiểm chứng; kịch bản test trong `../../research/competitive-kiem-ke-kho-sapo-kiotviet-cukcuk-2026-09-21/kich-ban-test-trong-san-pham.md` sẽ chốt được.
