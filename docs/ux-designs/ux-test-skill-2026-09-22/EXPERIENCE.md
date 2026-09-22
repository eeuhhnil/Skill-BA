---
status: draft
updated: 2026-09-22
sources:
  - docs/brainstorming/brainstorm-quan-ly-ca-ket-ca-2026-09-22/brainstorm-intent.md
  - docs/briefs/brief-test-skill-2026-09-22/brief.md
  - docs/research/competitive-sapo-va-kiotviet-quan-ly-ca-ket-ca-2026-09-22/research.md
---

# Quản lý ca, kết ca — EXPERIENCE.md

> Bản nháp đầu tiên, đánh dấu `[ASSUMPTION]` ở mọi chỗ mình tự suy luận từ brief + nghiên cứu đối thủ, chưa qua xác nhận của bạn. Giai đoạn này chỉ dừng ở phác thảo hành vi/cấu trúc (đen trắng) — chưa động đến bộ nhận diện màu sắc/thị giác (xem DESIGN.md).

## Foundation

- **Form factor:** Desktop. Một ứng dụng POS duy nhất (EasyPOS) dùng chung cho cả 3 vai — thu ngân, quản lý cửa hàng, chủ cửa hàng — không có bề mặt riêng cho từng vai ở phase này. `[ASSUMPTION, theo brief đã chốt]`
- **UI system:** Chưa xác định — EasyPOS có design system riêng trên Figma nhưng phiên UX này chủ động **chưa** kế thừa nó (theo yêu cầu của bạn: vẽ phác thảo trước). DESIGN.md hiện để trống/placeholder; việc tô màu theo design system EasyPOS sẽ làm ở bước sau.
- **Ngôn ngữ:** Tiếng Việt duy nhất. `[ASSUMPTION]`

## Kiến trúc thông tin (Information Architecture)

4 bề mặt (surface) chính, ánh xạ trực tiếp từ mục 2 "Yêu cầu nghiệp vụ" của brief:

1. **Mở ca** (thu ngân) — panel/modal xuất hiện ngay sau đăng nhập, trước khi vào màn bán hàng.
2. **Trạng thái ca / Trong ca** (thu ngân) — không phải màn hình riêng, mà là một badge trạng thái + số liệu chỉ-xem gắn trên thanh điều hướng của màn bán hàng. `[ASSUMPTION — vì brief nói "Trong ca chỉ đơn giản là xem", không cần một trang riêng]`
3. **Kết ca** (thu ngân) — panel/modal, mở từ nút "Kết ca" trên màn bán hàng.
4. **Danh sách ca + Chi tiết ca** (quản lý cửa hàng) — một trang quản trị riêng, danh sách có bộ lọc, click vào một dòng mở panel/trang chi tiết.

*(Chủ cửa hàng không có bề mặt riêng trong scope MUST hiện tại — brief đã hoãn "Báo cáo doanh thu tổng hợp".)*

## Component Patterns (hành vi)

- **Ô nhập tiền mặt** (đầu ca, kết ca): chỉ nhận số, tự format phân cách nghìn, không cho số âm.
- **Badge trạng thái ca:** 3 trạng thái — *Chưa mở ca / Đang mở ca / Đã đóng ca* — luôn hiển thị trên thanh điều hướng khi thu ngân đang đăng nhập.
- **Ô chênh lệch:** luôn là **tính toán tự động, chỉ đọc** (không cho sửa tay) = (đầu ca + phát sinh) − tiền đếm được. Có trạng thái thị giác riêng khi khác 0 so với khi bằng 0 (chi tiết màu sắc ở DESIGN.md sau).
- **Ô lý do chênh lệch:** textarea, **bắt buộc** khi chênh lệch ≠ 0, ẩn hoặc không bắt buộc khi = 0.
- **Đính kèm ảnh chứng từ:** control chọn file (không bắt buộc phải chụp trực tiếp qua webcam ở bản đầu) — 1 hoặc nhiều ảnh. `[ASSUMPTION]`
- **Bảng danh sách ca:** có bộ lọc (khoảng thời gian, trạng thái, nhân viên) phía trên; dòng có chênh lệch được đánh dấu trực quan để quản lý nhận ra ngay không cần mở từng dòng. `[ASSUMPTION]`
- **Nút In phiếu kết ca:** xuất hiện sau khi xác nhận kết ca thành công.

## State Patterns

- **Trạng thái ca:** Chưa mở ca → Đang mở ca → Đã đóng ca (một chiều, không quay lại).
- **Trạng thái chênh lệch:** Khớp (chênh lệch = 0, không cần lý do) / Có lệch (≠ 0, bắt buộc lý do trước khi xác nhận kết ca được).
- **Validation chặn:** Nút "Xác nhận kết ca" bị vô hiệu hóa cho tới khi (a) đã nhập tiền đếm được, và (b) nếu có lệch — đã nhập lý do. `[ASSUMPTION]`

## Interaction Primitives

- Mở ca và kết ca đều có **bước xác nhận rõ ràng** (không tự động lưu khi rời khỏi trường nhập) — tránh xác nhận nhầm với thao tác tiền bạc. `[ASSUMPTION]`
- Toàn bộ luồng thao tác được ở tốc độ quầy (nhập nhanh bằng bàn phím số, Enter để xác nhận) — vì thu ngân thao tác dưới áp lực thời gian (root cause đã xác định ở Five Whys). `[ASSUMPTION]`

## Accessibility Floor (hành vi)

- Toàn bộ luồng mở ca/kết ca thao tác được hoàn toàn bằng bàn phím, không bắt buộc chuột.
- Trạng thái chênh lệch không chỉ dựa vào màu sắc để truyền đạt — luôn kèm text ("Có chênh lệch: +/-X đ") để không phụ thuộc thị giác màu.
- Số liệu tài chính ưu tiên cỡ chữ đủ lớn, dễ đọc nhanh trong lúc thao tác vội.

`[ASSUMPTION]` toàn mục — chưa xác nhận với bạn, đặc biệt phần độ tương phản/màu sắc cụ thể sẽ chốt cùng design system EasyPOS ở bước sau.

## Luồng chính (Key Flows)

### 1. Lan (thu ngân) mở ca đầu ngày
Lan đăng nhập vào EasyPOS đầu ca sáng. Hệ thống chặn không cho vào màn bán hàng cho tới khi mở ca — hiện panel "Mở ca làm việc". Lan đếm tiền trong ngăn kéo, nhập vào ô "Số tiền mặt đầu ca", nhấn "Xác nhận mở ca". Panel đóng lại, màn bán hàng hiện ra với badge "Ca: Đang mở — Lan" trên thanh điều hướng.
**Đỉnh điểm:** toàn bộ thao tác dưới 10 giây — không cản trở việc mở cửa hàng đúng giờ.

### 2. Lan kết ca cuối ngày, có chênh lệch
Cuối ca, Lan nhấn "Kết ca" trên thanh điều hướng. Panel "Đóng ca làm việc" hiện ra, đã hiển thị sẵn tiền đầu ca và tiền phát sinh trong ca (hệ thống tự tính). Lan đếm tiền mặt thực tế trong ngăn kéo, nhập vào ô "Số tiền mặt đếm được". Hệ thống lập tức tính và hiện ô "Chênh lệch" — lần này khác 0. Ô "Lý do chênh lệch" tự động hiện ra và bắt buộc điền; Lan nhớ lại một lần trả tiền thừa nhầm cho khách, ghi lý do, đính kèm ảnh biên lai liên quan, rồi nhấn "Xác nhận kết ca". Hệ thống in phiếu kết ca có đầy đủ số liệu và lý do.
**Đỉnh điểm:** thay vì hoảng khi thấy số bị lệch, Lan có ngay tại chỗ một nơi để giải thích — cô cảm thấy **được bảo vệ**, không phải bị buộc tội.

### 3. Hùng (quản lý cửa hàng) tra cứu cuối ngày
Cuối ngày, Hùng mở "Danh sách ca làm việc", lọc theo hôm nay và trạng thái "Đã đóng". Anh thấy ngay dòng ca của Lan được đánh dấu có chênh lệch. Anh click vào, mở "Chi tiết ca" — thấy đầy đủ tiền đầu ca, tiền phát sinh, tiền kết ca, chênh lệch, lý do Lan đã ghi, và ảnh chứng từ đính kèm.
**Đỉnh điểm:** Hùng có đủ căn cứ trả lời ngay nếu chủ cửa hàng hỏi — không cần lục giấy tờ hay gọi lại hỏi Lan, đúng thứ quy trình giấy/Excel cũ không cho anh làm được.

## Wireframe (phác thảo đen trắng)

- Luồng thu ngân (mở ca → kết ca có chênh lệch → in phiếu): [.working/flow-thu-ngan-mo-ket-ca-2026-09-22.excalidraw](.working/flow-thu-ngan-mo-ket-ca-2026-09-22.excalidraw)
- Luồng quản lý (danh sách ca → chi tiết ca): [.working/flow-quan-ly-tra-cuu-ca-2026-09-22.excalidraw](.working/flow-quan-ly-tra-cuu-ca-2026-09-22.excalidraw)

*(Mở bằng Excalidraw desktop hoặc excalidraw.com.)*
