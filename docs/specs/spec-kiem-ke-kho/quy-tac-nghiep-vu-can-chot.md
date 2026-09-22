# Quy tắc nghiệp vụ cần chốt

Companion của `SPEC.md`. Mỗi mục dưới đây là một quyết định nghiệp vụ **chưa có lời giải**, mỗi lựa chọn kéo theo mô hình dữ liệu hoặc hành vi khác nhau. Phải trả lời trước khi viết mô tả chức năng.

Hai quy tắc đã chốt (mã chưa đếm, trạng thái phiếu) không nằm ở đây — chúng đã thành Constraint và CAP-9 trong `SPEC.md`.

---

## ✅ QT-1 — Giá áp cho phần thừa/thiếu — **ĐÃ CHỐT 2026-09-21**

**Ảnh hưởng:** CAP-8, CAP-13

**Quyết định: (a) — giá vốn tại thời điểm cân bằng kho.** Không dùng giá vốn tại snapshot, không dùng giá nhập gần nhất.

**Hệ quả cần biết khi đặc tả:** nếu một đợt kiểm kê kéo dài và giá vốn thay đổi giữa chừng, giá trị chênh lệch sẽ được tính theo giá vốn *mới* chứ không phải giá vốn lúc chốt snapshot. Đây là hệ quả có chủ đích.

**Cạm bẫy cần tránh khi hiện thực:** ở Sapo, đưa một lô về 0 sẽ reset giá vốn của lô đó về 0. Đừng lặp lại.

---

## ✅ QT-2 — Định nghĩa "tồn hệ thống tại thời điểm T" — **ĐÃ CHỐT 2026-09-21**

**Ảnh hưởng:** CAP-2, CAP-3, CAP-4, CAP-5, CAP-8

Đây từng là câu hỏi nặng nhất của cả nghiệp vụ. Lời giải gồm bốn phần:

### 1. Không liệt kê loại chứng từ

**Mọi bản ghi trong sổ chuyển động tồn kho chạm vào bộ ba `(kho, mã hàng, lô)` đều được tính, bất kể chứng từ nào sinh ra nó.**

Lý do bác phương án liệt kê: sang năm có thêm *hàng đổi bảo hành*, *xuất dùng nội bộ*, *điều chỉnh từ sàn TMĐT*… một danh sách cứng sẽ bỏ sót, và bỏ sót một loại nghĩa là tồn sai âm thầm — đúng kiểu lỗi không ai phát hiện.

### 2. Chốt tại thời điểm đếm từng dòng, không replay

Khi một dòng được đếm, hệ thống ghi **đồng thời** số thực đếm và **tồn hệ thống của đúng mã/lô đó tại đúng giây phút ấy**. Chênh lệch của dòng **đóng băng ngay tại đó**.

Lý do bác phương án *snapshot cấp đợt rồi tua ngược*: nhân viên đếm mã A lúc 9h, mã B lúc 15h — số họ đếm là tồn vật lý tại lúc đếm, không phải tại T0. Muốn so với T0 thì vẫn phải có mốc thời gian từng dòng; mà đã có mốc từng dòng rồi thì việc replay trở nên thừa.

Chốt từng dòng còn giải thích được bằng một câu cho thủ kho: *"14h32 hệ thống nói 20, anh đếm 18, thiếu 2."*

**Snapshot cấp đợt (CAP-2) vẫn giữ**, nhưng đổi vai: làm tiêu đề biên bản *"kiểm kê tại thời điểm T0"*, và làm cơ sở cho những mã **chưa đếm dòng nào** — vốn không có mốc thời gian riêng.

### 3. Mốc thời gian

Dùng **thời điểm chứng từ tác động vào sổ tồn**, không phải thời điểm tạo chứng từ. Snapshot đọc từ chính sổ đó, nên hai vế phải cùng một cơ sở thời gian thì mới khớp.

### 4. Hai cái bẫy phải xử lý

- **Chứng từ ghi lùi ngày** → **chặn** ghi lùi vào khoảng thời gian có phiếu kiểm kê đang mở trên kho đó. POS hiếm khi cần ghi lùi, còn cái giá của việc không chặn là một loại lỗi không lần ra được.
- **Nhập từ Excel không có thời điểm đếm thật** → bắt khai **một thời điểm đếm cho cả lô import**, mặc định là thời điểm import nhưng sửa được. Cửa hàng đếm giấy lúc 8h rồi nhập lúc 17h mà không khai thì toàn bộ giao dịch bán trong ngày bị tính nhầm thành chênh lệch.

### Bảng tra cho bảy loại giao dịch ban đầu

| Loại | Tính không | Lưu ý |
|---|---|---|
| Bán tại POS | ✅ tự động | Nằm trong sổ |
| Trả hàng từ khách | ✅ tự động | *Khi nào* hàng trả vào lại tồn là câu của `QT-9` |
| Nhập hàng NCC | ✅ tự động | |
| Trả hàng cho NCC | ✅ tự động | |
| Chuyển kho — bên gửi | ✅ tự động | |
| Chuyển kho — bên nhận | ✅ khi ghi nhận | **Hàng trên đường không thuộc kho nào** cho tới khi bên nhận ghi nhận |
| Hủy hàng | ✅ tự động | |
| Khuyến mãi / quà tặng xuất kho | ✅ nếu có ghi sổ tồn | Nếu đang xuất mà **không** ghi sổ thì đó là lỗi có sẵn — kiểm kê sẽ phơi nó ra |

> ⚠️ Dòng **chuyển kho bên nhận** là phán quyết theo khuyến nghị kỹ thuật, không phải do BA tự nêu. Nếu nghiệp vụ chuyển kho hiện tại của sản phẩm xử lý khác, đây là chỗ cần xem lại đầu tiên.

---

## ✅ QT-3 — Log việc xóa phiếu Chưa xử lý — **ĐÃ CHỐT 2026-09-21**

**Ảnh hưởng:** CAP-12, CAP-14

**Quyết định: (a) — không ghi log gì cả, xóa thẳng.** Không có quyền xóa riêng, không có bản ghi việc xóa.

**Rủi ro đã được nêu và được chấp nhận:** nghiệp vụ không có bước duyệt, nên xóa phiếu nháp là đường duy nhất để một người giấu kết quả bất lợi mà không để lại dấu vết. Nghĩa là **kiểm kê phát hiện được sai sót nhập liệu, nhưng không phát hiện được người cố tình giấu.** Ghi lại ở đây để người đọc sau hiểu đây là lựa chọn có ý thức, không phải sót.

---

## ~~QT-4 — Ngưỡng lệch định nghĩa ở cấp nào~~ — RÚT 2026-09-21

Không còn câu hỏi: **CAP-11 đã bị loại khỏi phạm vi**, nên khái niệm ngưỡng lệch không tồn tại trong spec này. Mã QT-4 không tái sử dụng.

---

## QT-5 — Người giữ kho có được đếm chính kho mình giữ không

**Ảnh hưởng:** CAP-12

- (a) Cho phép, nhưng không cấp quyền **cân bằng kho** cho người đó
- (b) Cấm hoàn toàn
- (c) Cho phép, không ràng buộc gì

**Lưu ý:** vì đã bỏ bước duyệt, phương án (a) chỉ có tác dụng nếu quyền cân bằng kho thực sự giao cho người khác. Nếu một người có cả hai quyền thì kiểm kê mất tác dụng kiểm soát thất thoát.

---

## QT-6 — Phiếu treo quá lâu sau cut-off

**Ảnh hưởng:** CAP-2

- (a) Tự hủy
- (b) Chỉ cảnh báo, vẫn cho cân bằng
- (c) Chặn cân bằng, bắt tạo đợt mới với snapshot mới

Kèm theo: ngưỡng "quá lâu" là bao nhiêu, và tính theo giờ hay theo ngày làm việc.

---

## ~~QT-7 — Xử lý mã lạ sau đợt kiểm kê~~ — RÚT 2026-09-21

Không còn câu hỏi: **CAP-7 đã bị loại khỏi phạm vi**, mã lạ quét ra trong lúc đếm không được ghi nhận. Mã QT-7 không tái sử dụng.

**Vẫn giữ lại một lưu ý cho phase sau:** nếu sản phẩm mở rộng sang khách hàng nhà thuốc và khi đó mở lại khả năng ghi nhận mã/lô mới phát sinh, điều đó xung đột trực tiếp với ràng buộc liên thông CSDL Dược — lô chưa khai báo sẽ bị hệ thống quốc gia từ chối đồng bộ.

---

## QT-8 — Điều chỉnh khi tổng khớp nhưng lệch giữa các lô

**Ảnh hưởng:** CAP-6, CAP-13

- (a) Một cặp điều chỉnh tăng lô này / giảm lô kia, giá trị tiền bằng 0
- (b) Hai chứng từ độc lập
- (c) Yêu cầu người cân bằng kho xác nhận riêng cho nhóm này

---

## QT-9 — Hàng có mặt vật lý nhưng chưa được ghi nhận nhập kho

**Ảnh hưởng:** CAP-2, CAP-13

Ví dụ: hàng khách trả đang chờ xử lý, hàng nhà cung cấp mới giao chưa lên phiếu nhập.

- (a) Đếm, và để lộ ra thành chênh lệch thừa
- (b) Loại trừ bằng cách đánh dấu trạng thái hàng
- (c) Yêu cầu hoàn tất chứng từ nhập trước khi chốt snapshot
