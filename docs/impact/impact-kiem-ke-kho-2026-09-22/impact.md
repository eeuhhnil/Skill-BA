---
title: Kiểm kê kho — Phân tích ảnh hưởng
type: impact-analysis
feature: kiem-ke-kho
status: draft
created: 2026-09-22
updated: 2026-09-22
source_doc: "docs/briefs/brief-kiem-ke-kho-2026-09-22/brief.md (tham chiếu docs/specs/spec-kiem-ke-kho/SPEC.md)"
confluence_space: EP
scan: "276 trang khớp / ~40 trang đã đọc; 52 từ khóa trong 5 nhóm (xem mục D)"
---

# Kiểm kê kho — Phân tích ảnh hưởng

> **Tóm tắt.**
> - Trên Confluence **đã có đặc tả Kiểm kê kho** (web v62, mobile, thiết kế cơ sở dữ liệu). Đặc tả này khác brief ở 6 điểm then chốt, trong đó nặng nhất là cách chốt tồn và việc cho **ghi lùi ngày kiểm kê**.
> - Ba ảnh hưởng lớn nhất:
>   - Cân bằng kho **đẩy tồn lên Shopee** và có thể **xung đột với EasyBooks**.
>   - Phiếu kiểm kê ghi lùi ngày làm đổi **báo cáo XNT, giá xuất kho và phụ lục tồn kho của tờ khai thuế** ở các kỳ cũ.
>   - Hệ thống đang có **ít nhất 4 đường sửa tồn khác** ngoài kiểm kê.
> - Đang chặn: phải chọn **brief hay đặc tả Confluence là bản chuẩn** (xem C-1).

Ký hiệu nguồn: `[pageId]` = trang Confluence `https://confluence-sds.softdreams.vn:8090/pages/viewpage.action?pageId=<pageId>`. Tên trang ghi kèm lần đầu.

## A. Tài liệu hiện có về chính nghiệp vụ này

| Trang | Phiên bản | Sửa cuối |
|---|---|---|
| Kiểm kê kho (đặc tả web) `[50698190]` | v62 | 21/09/2026, Dương Thị Huệ Linh |
| Kiểm kê kho – mobile `[50708685]` | v9 | 15/09/2026, Huệ Linh |
| Thiết kế cơ sở dữ liệu đề xuất `[50707019]` | v5 | 18/09/2026, Phạm Đức Thông |
| Dạo vòng quanh đối thủ `[50707840]` | v12 | 10/09/2026, Cao Bá Hướng |

Ngoài ra, PHÂN HỆ KHO HÀNG `[50697883]` đã liệt kê mục "5. Kiểm kê". Trang Số lô hạn dùng ver1 `[50698246]` ghi "Tính năng kiểm kho (Làm sau)".

→ **Tiền đề "phần mềm chưa có nghiệp vụ kiểm kê" trong brief (mục 1.3) không còn đúng về mặt tài liệu.** Nghiệp vụ đã được đặc tả, nhưng chưa rõ đã code chưa (cần dev xác nhận).

**Khác biệt giữa brief và đặc tả Confluence:**

| Điểm | Brief | Đặc tả Confluence | Nguồn |
|---|---|---|---|
| Chốt tồn hệ thống | Chốt tại lúc đếm từng dòng, sau đó đóng băng | Lấy `inventory.onhand` hiện tại; **nạp lại mỗi lần mở phiếu nháp** (BR-kiemke-005) | `[50698190]` §3.2 |
| Ngày chứng từ | Chặn ghi lùi ngày khi có phiếu mở | **Cho chọn ngày kiểm kê ≤ hôm nay**; `rs_inoutward.date` lấy theo ngày kiểm kê (BR-013) | `[50698190]` |
| Giá vốn tính chênh lệch | Giá vốn tại lúc cân bằng | `cogs_history` của kỳ chứa ngày kiểm kê; không có thì lùi về kỳ trước (BR-006) | `[50698190]` |
| Phạm vi | Toàn kho / ngành hàng / NCC / chọn tay; chặn đợt chồng lấn | Tất cả sản phẩm / chọn sản phẩm; không nói gì về chồng lấn | `[50698190]` §3.2 |
| Quyền | 6 quyền (có Nhập Excel) | Xem/Tạo/Sửa/Xóa/Cân bằng kho, cộng In và Xuất Excel (BR-002); bảng §3.5 **thiếu dòng Cân bằng kho** | `[50698190]` |
| Import Excel | Có trong phase này | Để phase sau | `[50698190]` §2.2 |
| Nền tảng | Web responsive, chưa làm app | **Có đặc tả app mobile** | `[50708685]` |
| Mã chưa đếm | Hỏi người dùng; giữ nguyên tồn | Hỏi người dùng; loại các mã đó khỏi phiếu → **khớp nhau** | `[50698190]` #29 |
| Serial/IMEI | Ngoài phạm vi | Không kiểm kê (BR-017) → **khớp nhau** | `[50698190]` |

## B1. Đánh giá tác động theo từng chiều

### Quy trình nghiệp vụ
- **Quy trình nào bị thay đổi?**
  - Thêm quy trình Kiểm kê kho.
  - Các quy trình đang **sửa tồn ngoài luồng** phải được xem lại để quyết giữ hay gom về kiểm kê:
    - Điều chỉnh tồn thủ công qua `adjust_inv` `[50697953]`
    - Sửa tồn trên màn sản phẩm / biến thể `[50698216]`
    - Cập nhật tồn qua file import `[50698113]`
    - Điều chỉnh tồn theo lô trên màn sản phẩm (N3/X2) `[50698238]`
- **Bước nào bị thêm / xóa / sửa?**
  - Bán hàng, nhập, xuất, chuyển kho, trả hàng: không đổi bước.
  - Nếu theo brief: **thêm bước chặn ghi lùi ngày** khi kho có phiếu kiểm kê đang mở. *Suy luận — cần xác nhận với từng luồng.*
  - Tính giá xuất kho: phải xử lý riêng phiếu kiểm kê `[50698190]` §4.1 · `[50698161]`.
- **Ai cần thay đổi cách làm việc?**
  - Quản lý kho / quản lý cửa hàng: kiểm kê bằng phiếu thay cho việc sửa tồn trực tiếp `[50698190]` §1.
  - Chủ shop có kết nối Shopee: cần biết cân bằng kho sẽ đổi tồn trên sàn `[50703337]`.
  - Kế toán dùng EasyBooks: cần biết việc kiểm kê làm ở hệ thống nào `[50698206]`.

### Hệ thống / Kỹ thuật
- **Module / service nào cần sửa?**
  - Kho: thêm mới Kiểm kê.
  - Tính giá xuất kho `[50698161]`.
  - Báo cáo XNT và XNT theo lô `[50698057]` `[50698078]`.
  - Đồng bộ Shopee v2 và Đa kho sàn `[50703337]` `[50704714]`.
  - Tích hợp EasyBooks `[50698206]`.
  - Liên thông CSDL Dược `[50697897]` `[50698048]`.
  - Phân quyền `[50698180]`.
  - Mẫu in, trong phần cấu hình cửa hàng `[50698190]` §3.6.
- **API, database schema, UI nào thay đổi?**
  - Thêm bảng `inventory_check` và `inventory_check_detail` `[50707019]`.
  - `rs_inoutward` thêm liên kết `type_doc`/`ref_id` về phiếu kiểm kê `[50707019]`.
  - Thêm mã loại nghiệp vụ `business_type` cho phiếu nhập/xuất do kiểm kê sinh ra. *Chưa trang nào định nghĩa mã này.*
  - Thêm quyền mới vào bảng `permission`; trang Chuyển kho có ghi "thêm bộ quyền chuyển kho, kiểm kê kho" `[50698018]`.
  - UI: danh sách phiếu, tạo phiếu 2 bước, popup chọn lô, 2 popup khi cân bằng, trên cả web lẫn mobile `[50698190]` `[50708685]`.
- **Tích hợp bên ngoài nào bị ảnh hưởng?**
  - **Shopee:** v2 lấy tồn POS làm gốc và liệt kê "kiểm kho" là một biến động được đẩy lên sàn `[50703337]`. Bản v1 (sàn làm gốc) thì không đẩy lên sàn `[50697946]`.
  - **EasyBooks:** khi đã kết nối, chức năng nhập/xuất kho thuần trên POS bị khóa và tồn đi theo EB `[50698206]` §2–3.1.
  - **CSDL Dược:** có cấu hình `autoPushRsInWard` / `autoPushRsOutWard` tự đẩy phiếu nhập/xuất `[50698048]`.

### Dữ liệu
- **Dữ liệu hiện tại có cần migrate không?**
  - Không cần chuyển đổi dữ liệu cũ, vì chỉ thêm bảng mới `[50707019]`.
  - Nếu quyết định gom các đường sửa tồn cũ về kiểm kê thì phải quyết định lịch sử `adjust_inv` và các phiếu "sửa tồn kho" cũ hiển thị ở đâu. *Suy luận.*
- **Có thay đổi validation rules không?**
  - Có. Tồn thực tế ≥ 0; mỗi phiếu gắn đúng một kho; phiếu Đã xử lý không sửa, không xóa; không kiểm kê Serial/IMEI `[50698190]` BR-004→017.
  - Nếu theo brief: thêm quy tắc chặn ghi lùi ngày ở mọi luồng có chứng từ kho.
  - **Cho xuất quá tồn** (`overStock`) làm tồn hệ thống có thể âm khi kiểm kê `[50698068]`.
- **Báo cáo, dashboard nào bị ảnh hưởng?**
  - Xuất – Nhập – Tồn và XNT theo lô: cộng theo `rsi.date` và loại phiếu 1/2/3 `[50698057]` `[50698078]` → cần thêm loại phiếu kiểm kê; phiếu ghi lùi ngày làm đổi tồn đầu kỳ của kỳ sau.
  - **Tờ khai thuế phụ lục 01/BK-HTK:** lấy báo cáo tồn kho đến ngày 31/12/2025 `[50698012]` §3.5 · `[50697930]` → kiểm kê ghi lùi vào năm 2025 sẽ làm đổi số liệu trên tờ khai.
  - Lợi nhuận sản phẩm: dùng giá vốn, nên bị ảnh hưởng gián tiếp khi tính lại giá xuất kho `[50698243]`.
  - Thống kê tồn kho / Báo cáo chi tiết tồn kho: có mã quyền 270105, 270109 `[50698180]`, nhưng *chưa đọc đặc tả của hai báo cáo này*.

### Con người
- **Ai cần được training?** Quản lý kho, quản lý cửa hàng, nhân viên kho (vai trò `ROLE_INVENTORY`) `[50698180]`. Kế toán (nếu dùng EasyBooks). Đội CS/triển khai cho các khách có kết nối Shopee, EasyBooks hoặc CSDL Dược.
- **Có thay đổi về quyền / roles không?** Có: thêm bộ quyền kiểm kê. Cần chốt quyền mặc định cho `ROLE_ADMIN` và `ROLE_INVENTORY` `[50698180]`. Đặc tả hiện chỉ gán cho Quản lý kho và Quản lý cửa hàng `[50698190]` §3.5.
- **Stakeholder nào cần được thông báo?**
  - Huệ Linh (BA Kiểm kê, XNT theo lô, Phân bổ lô).
  - Vũ Khánh Huyền (BA Sàn TMĐT, Combo).
  - Trần Thị Hồng Hạnh (XNT, Tờ khai thuế, SP sản xuất, EasyBooks nội bộ).
  - Nguyễn Hạnh Kiều Trang (CSDL Dược).
  - Nguyễn Thành Trung (Offline mobile).
  - Phạm Đức Thông (thiết kế cơ sở dữ liệu).
  - Cao Bá Hướng (dev).

## B2. Ma trận đánh giá tác động

*Nỗ lực S/M/L/XL là ước lượng của BA để xếp thứ tự ưu tiên, **không phải estimate của dev**.*

| Thành phần bị ảnh hưởng | Loại tác động | Mức độ | Nỗ lực ước tính | Rủi ro | Nguồn | Ai xác nhận |
|---|---|---|---|---|---|---|
| Kiểm kê kho (web + mobile) | Thêm mới | High | XL | Hai tài liệu (brief và đặc tả) mâu thuẫn nhau → dev làm theo bản nào? | `[50698190]` `[50708685]` | PO + Huệ Linh |
| Cơ sở dữ liệu: `inventory_check*`, liên kết `rs_inoutward` | Thêm mới | High | M | `type_doc` ghi 3 hay 4 chưa thống nhất | `[50707019]` | Phạm Đức Thông |
| Phiếu nhập/xuất (`rs_inoutward`, `business_type`) | Sửa đổi | High | S | Chưa có mã loại nghiệp vụ cho kiểm kê; báo cáo không nhận diện được loại phiếu | `[50697953]` `[50698190]` §4.2 | Dev |
| Tính giá xuất kho | Sửa đổi | High | M | Phiếu kiểm kê bị tính lại giá sai, hoặc bị loại sai khỏi phép tính giá | `[50698190]` §4.1 · `[50698161]` | Dev + BA kho |
| Báo cáo XNT, XNT theo lô | Sửa đổi | High | S | Ghi lùi ngày làm đổi số liệu các kỳ đã chốt | `[50698057]` `[50698078]` | Hồng Hạnh / Huệ Linh |
| Tờ khai thuế (phụ lục tồn kho 01/BK-HTK) | Sửa đổi (gián tiếp) | High | S | Số tồn trên tờ khai không khớp với số đã nộp | `[50698012]` `[50697930]` | Hồng Hạnh + PO |
| Đồng bộ tồn Shopee v2 / Đa kho | Sửa đổi | High | M | Cân bằng kho ghi đè tồn trên sàn; đếm sai thì bán vượt hoặc bị ẩn tin đăng | `[50703337]` `[50704714]` | Khánh Huyền |
| Tích hợp EasyBooks | Sửa đổi | High | L | POS sinh phiếu kho trong khi EB là nơi làm chủ tồn → lệch giữa hai hệ thống | `[50698206]` | Hồng Hạnh + PO |
| Liên thông CSDL Dược | Sửa đổi | Med | M | Phiếu kiểm kê tự đẩy lên CSDL Dược (dù brief để nhà thuốc ngoài phạm vi) | `[50698048]` `[50697897]` | Kiều Trang |
| Các đường sửa tồn khác (`adjust_inv`, sửa tồn trên màn sản phẩm/biến thể, import, phân bổ lô) | Sửa đổi / Xóa (cần quyết) | Med | M | Còn đường sửa tồn tự do → kiểm kê mất ý nghĩa kiểm soát | `[50697953]` `[50698216]` `[50698113]` `[50698238]` | PO |
| Cập nhật tồn bất đồng bộ (`inventory_log`) | Sửa đổi (kiểm tra) | Med | S | Tồn hệ thống lúc đếm chưa trừ các log đang chờ xử lý | `[50697953]` | Dev |
| Bán offline trên mobile | Sửa đổi (kiểm tra) | Med | S | Đơn offline đồng bộ muộn → chênh lệch giả | `[50698029]` | Thành Trung |
| Cho phép xuất quá tồn | Sửa đổi (kiểm tra) | Low | S | Tồn hệ thống âm hiển thị trên phiếu | `[50698068]` | BA kho |
| Loại sản phẩm: combo, liệu trình, thành phẩm định mức, dịch vụ | Sửa đổi (lọc) | Med | S | Đưa nhầm sản phẩm không có tồn riêng vào phiếu | `[50698140]` `[50698079]` `[50698254]` `[50697958]` | BA sản phẩm |
| SP sản xuất / NVL | Sửa đổi | Low | S | Phải kiểm kê được (tài liệu ghi "có kiểm kê") | `[50698254]` | Hồng Hạnh |
| Số khung số máy | Sửa đổi (lọc) | Low | S | Có cơ chế định danh giống IMEI nhưng chưa có trong BR-017 | `[50698116]` | Hồng Hạnh |
| Phân quyền | Thêm mới | Med | S | Thiếu quyền Cân bằng kho → ai có quyền Tạo cũng đổi được tồn | `[50698180]` `[50698190]` §3.5 | PO |
| Mẫu in phiếu kiểm kê | Thêm mới | Low | S | — | `[50698190]` §3.6 | Huệ Linh |

## B3. Dependency Map

```
[Kiểm kê kho → Cân bằng kho]
    ├── Phụ thuộc bởi:                                  ← dùng phiếu/tồn do kiểm kê sinh ra
    │     Tính giá xuất kho · Báo cáo XNT / XNT theo lô · Tờ khai thuế (phụ lục 01/BK-HTK)
    │     Lợi nhuận sản phẩm · Cảnh báo tồn / Kho hàng sàn
    ├── Phụ thuộc vào:                                  ← kiểm kê đọc / cần
    │     inventory.on_hand (qua inventory_log bất đồng bộ) · batches / lô – hạn dùng
    │     cogs_history (giá vốn theo kỳ) · product_product_unit (đơn vị tính, quy đổi)
    │     Danh mục kho · Phân quyền · Cấu hình cho xuất quá tồn
    │     Các luồng làm tồn thay đổi trong lúc đếm: bán hàng (kể cả offline), trả hàng,
    │       chuyển kho, lệnh sản xuất, liệu trình, đơn Shopee (webhook)
    └── Tích hợp với:                                   ← hệ thống ngoài
          Shopee (đẩy tồn v2, đa kho) · EasyBooks (nơi làm chủ tồn khi đã kết nối)
          CSDL Dược quốc gia (tự đẩy phiếu nhập/xuất)
```

## C. Mâu thuẫn và điểm cần quyết định

| # | Mâu thuẫn / câu hỏi | Giữa | Ai quyết | Trạng thái |
|---|---|---|---|---|
| 1 | **Bản nào là chuẩn: brief hay đặc tả v62?** Liên quan 6 điểm khác biệt ở mục A | Brief ↔ `[50698190]` | PO | [ ] |
| 2 | Cho ghi lùi ngày kiểm kê trong khi tồn lại lấy theo *hiện tại*. Ví dụ: chọn ngày 01/09 nhưng dùng tồn của ngày 22/09 → chênh lệch sai, và sai cả báo cáo lẫn tờ khai của kỳ cũ | `[50698190]` BR-005 ↔ BR-013 | PO + Huệ Linh | [ ] |
| 3 | Khách đã kết nối EasyBooks: chặn kiểm kê trên POS, đồng bộ phiếu kiểm kê sang EB, hay chỉ cho kiểm kê trên EB? | Kiểm kê ↔ `[50698206]` | PO + Hồng Hạnh | [ ] |
| 4 | Cân bằng kho có được đẩy tồn lên Shopee ngay không? Có cần hỏi xác nhận riêng không? | Kiểm kê ↔ `[50703337]` | PO + Khánh Huyền | [ ] |
| 5 | Phiếu kiểm kê có tự đẩy lên CSDL Dược không? (Brief để nhà thuốc ngoài phạm vi, nhưng khách nhà thuốc đang dùng hệ thống) | Kiểm kê ↔ `[50698048]` | Kiều Trang | [ ] |
| 6 | Giữ hay đóng 4 đường sửa tồn khác? Brief yêu cầu "không có đường sửa tồn tự do" | Brief ↔ `[50697953]` `[50698216]` `[50698113]` `[50698238]` | PO | [ ] |
| 7 | `rs_inoutward.type_doc` của kiểm kê là **3 hay 4**? Cùng một trang ghi cả hai giá trị. Đặc tả web lại dùng `rs_inoutward.type=4`, trong khi báo cáo XNT chỉ biết type 1/2/3 | `[50707019]` ↔ `[50698190]` §4.1 ↔ `[50698057]` | Phạm Đức Thông | [ ] |
| 8 | Công thức giá trị chênh lệch **ngược dấu**: *thực tế − hệ thống* ở `[50698190]`, nhưng *sổ sách − thực tế* ở `[50707019]` | Nội bộ Confluence | Huệ Linh + Thông | [ ] |
| 9 | BR-kiemke-013 nhắc tới `mc_receipt/mc_payment` (phiếu thu/chi). Kiểm kê có sinh phiếu thu/chi không, hay đây là lỗi sao chép? | `[50698190]` ↔ `[50698010]` | Huệ Linh | [ ] |
| 10 | Đặc tả kiểm kê đọc `batches_detail.on_hand`, nhưng tài liệu cơ sở dữ liệu (v1, 04/2026) không có cột này; tồn theo lô nằm ở `inventory.batch_id` | `[50698190]` ↔ `[50697953]` | Dev | [ ] |
| 11 | Số hiệu BR lệch giữa đặc tả web và thiết kế cơ sở dữ liệu (vd BR-006/007 về giá vốn, BR-009/008 về cấm sửa) | `[50698190]` ↔ `[50707019]` | Huệ Linh | [ ] |
| 12 | Tồn hệ thống đọc lúc đếm có tính các `inventory_log` đang ở trạng thái chờ (status = 0) không? | `[50697953]` | Dev | [ ] |
| 13 | Sản phẩm có số khung số máy có bị loại khỏi kiểm kê như IMEI không? | `[50698116]` ↔ BR-017 | PO | [ ] |
| 14 | Mã `business_type` cho phiếu sản xuất ghi không nhất quán (N10 ↔ N9, X10 ↔ X9) → cần thống nhất trước khi thêm mã cho kiểm kê | `[50698144]` ↔ `[50698254]` | Dev | [ ] |

## D. Phạm vi quét

- **Space:** EP. **Nhánh đã loại:** TestCase, Nâng cấp, Thay đổi giao diện.
- **Từ khóa (52 từ khóa, 5 nhóm):**
  - ① Chính nghiệp vụ: kiểm kê, kiểm kho, kiểm hàng, cân bằng kho, inventory_check.
  - ② Chiều ghi: đồng bộ tồn, update_stock, rs_inoutward, phiếu nhập/xuất kho, loại chứng từ, business_type, giá vốn, tính giá xuất kho, cogs, tồn đầu kỳ, xuất nhập tồn, báo cáo tồn, EasyBooks, dược quốc gia.
  - ③ Chiều đọc: tồn kho, on_hand, bán hàng, trả hàng, chuyển kho, hủy hàng, xuất hủy, sản xuất, offline, webhook, xuất quá tồn, sửa tồn, điều chỉnh tồn, ghép cặp, phiếu khởi tạo.
  - ④ Loại sản phẩm: lô, hạn dùng, hạn sử dụng, IMEI, serial, combo, định mức, liệu trình, nguyên vật liệu, đơn vị tính, biến thể.
  - ⑤ Phần bao quanh: phân quyền, permission, vai trò, mobile, mẫu in, cấu hình cửa hàng.
- **Kết quả:** 276 trang khớp. Đã lọc 100 trang đầu để tìm trang nhắc thẳng tới "kiểm kê" (12 trang). Đã đọc khoảng 40 trang:
  - Đọc đầy đủ: 4 trang Kiểm kê, trang cơ sở dữ liệu Nhóm 3.
  - Đọc trích đoạn: các trang còn lại được dẫn nguồn ở trên.
- **Khớp từ khóa nhưng bỏ qua vì không liên quan tới tồn:** Voice bán hàng, Chatbot, Tích hợp Shopee Express, Tối ưu tìm kiếm sản phẩm, Tự động đăng sản phẩm lên Shopee, Bảo hành (chỉ nhắc tới IMEI).
- **Giới hạn:**
  - Tài liệu Confluence mô tả thiết kế, **chưa chắc khớp với code đang chạy**. Đặc biệt tài liệu cơ sở dữ liệu Nhóm 3 là v1 từ 04/2026, có dấu hiệu đã cũ (C-10).
  - Chưa đọc: đặc tả hai báo cáo "Thống kê tồn kho" và "Báo cáo chi tiết tồn kho", các luồng Trả hàng / Hủy hàng chi tiết, trang UML của EasyBooks.
  - Các trang từ vị trí 101 trở đi trong danh sách xếp hạng chưa được lọc theo từ "kiểm kê".
