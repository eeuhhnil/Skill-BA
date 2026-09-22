# Sapo — Round 2 digest (kiểm kê kho)

Accessed: 2026-09-21. All claims below trace to a page fetched in this run.

**Biggest structural correction to round 1:** the current Sapo help centre organises stocktaking as a **separate installable app ("Ứng dụng Kiểm kho", apps.sapo.vn/stock-take) on Sapo OmniAI**, not as an in-product screen. The round-1 articles describe the older Sapo Omni (v2) / retail build. The help centre now carries both product lines side by side (Sapo Omni v2, Sapo OmniAI v3, Sapo FnB).

---

## Findings

### Gap 2 — `help.sapo.vn/ung-dung-kiem-kho` (RESOLVED, and it holds nothing)

- **claim:** The URL `help.sapo.vn/ung-dung-kiem-kho` resolves to an article titled **"Cài đặt ứng dụng kiểm kho trên Sapo OmniAI"** whose entire body is a 3-step *installation* procedure: go to `https://apps.sapo.vn/stock-take` → enter store domain (`abc.mysapo.net`) → approve permissions. Prerequisite: **"Chỉ tài khoản quản trị mới được kết nối lần đầu ứng dụng Kiểm kho."** The page contains **zero** occurrences of "phiếu kiểm", "Cân bằng", "tồn thực tế", or "chưa kiểm" (verified by string search of the raw HTML). Round 1's truncation concealed nothing — there is no counting-workflow content on this page.
  - source: https://help.sapo.vn/ung-dung-kiem-kho | publisher: Sapo (help centre) | pub_date: none shown (site footer © 2026) | accessed: 2026-09-21 | confidence: high | class: feature | variant: **Sapo OmniAI**

- **claim:** The real workflow article is a sibling: **`help.sapo.vn/cap-nhat-ton-kho-bang-ung-dung-kiem-kho-tren-sapo-omniai`**. The OmniAI warehouse overview lists exactly four articles under section "5. Kiểm kho & Ứng dụng kiểm kho": Cài đặt ứng dụng; Cập nhật tồn kho bằng ứng dụng kiểm kho; Xem, tìm và lọc phiếu kiểm kho; Kiểm kho cho sản phẩm có đơn vị quy đổi.
  - source: https://help.sapo.vn/tong-quan-cac-tinh-nang-quan-ly-san-pham-kho-hang-tren-sapo-omniai-1 | publisher: Sapo | pub_date: none shown | accessed: 2026-09-21 | confidence: high | class: feature | variant: Sapo OmniAI

### Gap 4a — Uncounted items at Cân bằng kho (ANSWERED, documented explicitly)

- **claim:** Uncounted lines are **NOT zeroed and NOT silently left alone — they are removed from the sheet, by explicit user choice.** On pressing **Cân bằng kho**, a "Xác nhận cân bằng" screen shows the number of uncounted items and offers two buttons: **"Loại bỏ và cân bằng"** (drop the uncounted products out of the sheet, then balance) or **"Tiếp tục kiểm"** (go back and keep counting). Exact text: *"Trường hợp, còn sản phẩm chưa kiểm, trên màn Xác nhận cân bằng sẽ hiển thị số lượng chưa kiểm... Nếu bạn muốn loại bỏ các sản phẩm chưa kiểm khỏi phiếu, bạn nhấn chọn Loại bỏ và cân bằng."* Net effect: an uncounted product's stock is **left unchanged**. Same behaviour documented for the mobile app.
  - source: https://help.sapo.vn/cap-nhat-ton-kho-bang-ung-dung-kiem-kho-tren-sapo-omniai | publisher: Sapo | pub_date: none shown | accessed: 2026-09-21 | confidence: high | class: feature | variant: Sapo OmniAI (desktop + mobile)

- **claim:** There is a dedicated **"Chưa kiểm kho" tab** in the sheet detail to work the remaining lines, plus a quick summary of **Đã kiểm / Khớp / Lệch** behind the 3-dot menu.
  - source: as above | confidence: high | class: feature | variant: Sapo OmniAI

### Gap 1 — Lô / hạn sử dụng in stocktaking (ANSWERED; richer than round 1, but NOT a separate Pharma product)

- **claim:** **There is no separate "Sapo Pharma / Sapo nhà thuốc" edition and no pharmacy-specific help section.** The help centre's product switcher lists only: Sapo OmniAI (v3), Sapo Omni (v2), Sapo FnB, Thiết bị bán hàng, Sản phẩm và dịch vụ khác, Sapo Accounting. Pharmacy is a **"Lĩnh vực kinh doanh" (business-field) setting** inside the standard product: Cấu hình > Thông tin cửa hàng > Lĩnh vực kinh doanh > **Nhà thuốc**. Warning in the doc: *"Hệ thống cho phép bạn chuyển đổi từ các loại hình kinh doanh khác sang mô hình Nhà thuốc, tuy nhiên không thể chuyển ngược lại từ Nhà thuốc về mô hình khác."* (one-way switch).
  - source: https://help.sapo.vn/lien-thong-nha-thuoc | publisher: Sapo | pub_date: none shown | accessed: 2026-09-21 | confidence: high | class: feature | variant: retail/Omni with Nhà thuốc business field

- **claim:** Drugs created via the Cục Quản lý Dược lookup are **lot-managed by default**: *"Thuốc tạo ra sẽ mặc định được quản lý theo lô - hạn sử dụng."* So a pharmacy's stocktaking is the **standard retail lô-HSD kiểm kho** — there is no pharma-specific count flow.
  - source: https://help.sapo.vn/lien-thong-nha-thuoc | confidence: high | class: feature

- **claim (notable negative):** The national drug database (CSDL Dược Quốc gia) sync covers **only four document types — "đơn nhập hàng, trả hàng nhà cung cấp, đơn hàng, khách trả hàng"** — triggered on xuất/nhập kho. **Phiếu kiểm kho / cân bằng kho is NOT in that list.** A stocktake write-off therefore appears not to be reported to the Dược Quốc gia system, which is a compliance gap worth probing.
  - source: https://help.sapo.vn/lien-thong-nha-thuoc | confidence: medium-high (the list is explicit and closed-form; absence of kiểm kho is inferred from that closed list, not separately stated) | class: feature

- **claim:** **Lot-level counting on desktop:** for lô-HSD products you press **"Chọn lô kiểm"** and enter counted quantity per lot. Doc advises: *"Bạn nên chọn đủ lô để kiểm để đảm bảo sản phẩm được kiểm hết, nếu không rất dễ sẽ bị sai sót."*
  - source: https://help.sapo.vn/cap-nhat-ton-kho-bang-ung-dung-kiem-kho-tren-sapo-omniai | confidence: high | class: feature | variant: Sapo OmniAI desktop

- **claim (new, beats round 1):** **Partially-counted lots get an explicit three-way prompt at balance time.** If a lot-managed product has lots selected but not all counted, a warning offers: (1) *"Chọn cân bằng số lượng tồn kho các lô chưa kiểm = 0"*; (2) *"Chọn cân bằng số lượng tồn kho các lô chưa kiểm bằng giá trị tồn kho hiện tại"* (leave unchanged); (3) *"Chọn Tiếp tục kiểm"*, which opens a tab filtered to just the products with uncounted lots. This is a **materially better uncounted-handling model at lot level than at product level** — at product level the only "zero it" path does not exist.
  - source: as above | confidence: high | class: feature | variant: Sapo OmniAI desktop

- **claim:** **The mobile app cannot count lot-managed products at all:** *"Hiện tại, tính năng kiểm kho trên ứng dụng di động chỉ hỗ trợ cho sản phẩm thường và sản phẩm có đơn vị quy đổi. Các sản phẩm dịch vụ, sản phẩm theo lô hay combo sẽ chưa được hỗ trợ trong phiên bản này."* For a pharmacy — whose entire catalogue is lot-managed by default — this means **the phone-based count is effectively unusable**; counting must be done on desktop.
  - source: as above | confidence: high | class: feature | variant: Sapo OmniAI mobile — **strongest competitive finding in this round**

- **claim:** **Expiry date (HSD) is not shown as a column in the counting grid** in the documented flow. The documented columns are: Tồn chi nhánh, Tồn thực tế, SL chênh lệch, Giá trị chênh lệch, Lý do. Lot selection is behind a "Chọn lô kiểm" dialog. No HSD/expiry surfacing during counting is described.
  - source: as above | confidence: medium (absence from an otherwise column-by-column description) | class: feature

- **claim (round-1 confirmation):** **Variance is shown in both quantity AND value.** Round 1 recorded variance as quantity-only; the OmniAI app documents **"Cột Giá trị chênh lệch: Hiển thị giá trị chênh lệch"** alongside **"Cột SL chênh lệch"**. Round 1's quantity-only reading should be corrected for the OmniAI variant.
  - source: as above | confidence: high | class: feature | variant: Sapo OmniAI

- **claim (round-1 confirmation):** **No blind counting, confirmed for OmniAI too.** The **"Tồn chi nhánh"** (system quantity) column is displayed next to the input field, and the doc's worked example tells the counter what the system shows before they type.
  - source: as above | confidence: high | class: feature

### Gap 3 — Pricing (NOW VERIFIED by direct fetch; round 1's figures were partly wrong)

- **claim:** Current published retail (Bán lẻ) tiers on `www.sapo.vn/bang-gia.html`: **StartUp 170.000đ/tháng; PRO 249.000đ/tháng; OMNI 449.000đ/tháng; ADVANCED 600.000đ/tháng; GROWTH 999.000đ/tháng; ENTERPRISE "Theo nhu cầu"**. Setup fees (phí khởi tạo): StartUp 1.000.000đ, Pro/Omni 1.500.000đ, Advanced 2.000.000đ, Growth 3.000.000đ — all waived on 2+ year contracts.
  - source: https://www.sapo.vn/bang-gia.html | publisher: Sapo | pub_date: **no effective date / "áp dụng từ" shown anywhere on the page** | accessed: 2026-09-21 | confidence: high for the numbers, low for how long they have stood | class: pricing

- **claim (correction to round 1):** Round 1's **"Omnichannel 599k"** is **not supported** by the published page — the OMNI tier is **449.000đ/tháng**. Round 1's "Start Up 249k→170k" conflates two product lines: **170k is the retail StartUp list price**, while **249k/170k is the FnB StartUp** price pair (*"249.000đ/tháng"* or *"170.000đ/tháng khi mua từ 2 năm"*). FnB Pro: 399.000đ/tháng, or 249.000đ/tháng at 2+ years.
  - source: as above | confidence: high | class: pricing

- **claim:** **Stocktaking is not a paid add-on.** The **Kiểm kho** app on the Sapo app store is listed as **free**, publisher "Sapo Apps". It is however **gated to the Sapo OmniAI platform** (the listing states OmniAI-only), so access depends on being on the OmniAI product line rather than on a price tier.
  - source: https://apps.sapo.vn/stock-take | publisher: Sapo Apps | pub_date: no version/last-updated shown | accessed: 2026-09-21 | confidence: medium-high | class: pricing

- **claim (trap — do not confuse):** The OMNI tier's advertised **"Quét kiểm hàng và Quét đóng gói"** is **order picking/packing scan at the order-processing screen** (`help.sapo.vn/quet-kiem-hang-tai-man-xu-ly-don-hang`), **not** stocktaking. "Kiểm hàng" in that pricing bullet means checking goods against an order, not counting inventory.
  - source: https://www.sapo.vn/bang-gia.html + link seen on https://help.sapo.vn/tong-quan-cac-tinh-nang-quan-ly-san-pham-kho-hang-tren-sapo-omniai-1 | confidence: medium-high | class: pricing

- **claim:** Sapo's pharmacy marketing page advertises **"Chỉ từ 170.000đ/tháng"** — i.e. the same retail StartUp entry price, no pharmacy premium — and links to the **general** `help.sapo.vn`, not to pharmacy-specific docs. It claims **"Chính thức liên thông cơ sở dữ liệu Dược Quốc gia"**.
  - source: https://www.sapo.vn/phan-mem-quan-ly-nha-thuoc.html | publisher: Sapo (marketing) | pub_date: none shown | accessed: 2026-09-21 | confidence: medium (sales-facing register) | class: pricing

### Other mechanics captured this run (all Sapo OmniAI)

- **claim:** Sheet scope at creation: Chọn sản phẩm cụ thể / Tất cả sản phẩm / Danh mục / Loại sản phẩm / **Tình trạng kho (Tồn kho > 0, = 0, < 0)**, or "Chọn sản phẩm sau" for an empty sheet built by scanning. So zero-stock and **negative-stock** products can be pulled deliberately into a sheet at product level.
  - source: https://help.sapo.vn/cap-nhat-ton-kho-bang-ung-dung-kiem-kho-tren-sapo-omniai | confidence: high | class: feature
- **claim:** Hard cap **10.000 sản phẩm per phiếu kiểm** (*"Hệ thống giới hạn tối đa 10,000 sản phẩm cho mỗi phiếu kiểm kho"*; app listing says *"lên đến 10.000 mã hàng/phiếu kiểm"*).
  - source: as above + https://apps.sapo.vn/stock-take | confidence: high | class: feature
- **claim:** Sheet gets an auto code (example **ST00179**) and enters status **"Đang kiểm kho"** on creation.
  - source: as above | confidence: high | class: feature
- **claim:** **A third permission exists** beyond round 1's two: access to the app is controlled by **"Ứng dụng - Kiểm kho"**, and there is a separate article *"Cấu hình phân quyền quản lý kho trên Sapo OmniAI"*. Still **no evidence of a count-vs-approve separation** — "Cân bằng kho" is pressed by whoever holds app access.
  - source: as above (prerequisites section) | confidence: medium-high | class: feature
- **claim:** **Auto-save on blur:** *"Sau khi nhập số lượng vào cột Tồn thực tế và click chuột vào vị trí bất kỳ trên màn hình thì hệ thống sẽ tự lưu thông tin phiếu của bạn."* Implies a server-side sheet, not a local draft.
  - source: as above | confidence: high | class: feature
- **claim (usability weakness):** *"Chức năng tìm kiếm chỉ áp dụng tìm kiếm sản phẩm đã có trong danh sách, không áp dụng cho việc thêm sản phẩm cần kiểm vào danh sách"* — the in-sheet search cannot pull in a product that is not already on the sheet.
  - source: as above | confidence: high | class: feature
- **claim:** Mobile counting by camera scan is **incremental** (+1 per successful scan), and on an empty sheet the **first scan adds the product at qty 1** — so a found-but-not-listed *product* can be added mid-count on mobile. (This does **not** extend to a found *lot*, since mobile excludes lot products entirely.)
  - source: as above | confidence: high | class: feature
- **claim:** A single **"Nhân viên kiểm"** field is set per sheet and is editable via "Sửa thông tin phiếu kiểm". One named counter per sheet.
  - source: as above | confidence: high | class: feature

---

## Leads

- `help.sapo.vn/xem-tim-va-loc-phieu-kiem-kho-tren-ung-dung-kiem-kho-tren-sapo-omniai` — **not fetched**. Most likely place to find the full **status list** for OmniAI phiếu kiểm kho (we only confirmed "Đang kiểm kho") and any filter-by-status enumerating a cancelled/balanced state.
- `help.sapo.vn/kiem-kho-cho-san-pham-co-don-vi-quy-doi` — **not fetched**. Conversion-unit counting; likely holds the rounding/conversion variance rules.
- `help.sapo.vn/cau-hinh-phan-quyen-quan-ly-kho-tren-sapo-omniai` — **not fetched**. Would settle the approval-separation question for OmniAI definitively.
- `help.sapo.vn/chinh-ton-kho-va-bo-luu-kho-lo-san-pham` — **not fetched**. Round 1 found that zeroing a lot resets its giá vốn to 0; this article is where that behaviour would be confirmed or bounded for OmniAI.
- `help.sapo.vn/quet-kiem-hang-tai-man-xu-ly-don-hang` — order picking scan, the OMNI-tier pricing bullet. Worth one fetch purely to avoid a competitor-comparison error.
- The **Sapo Omni (v2)** product line still has its own parallel doc tree. Round 1's findings are probably v2; the two lines should be reported as two different answers, not one.

## Looked for but could not find

- **Snapshot / cut-off (Gap 4a): genuinely undocumented.** Nothing in any page fetched states whether the **"Tồn chi nhánh"** column re-reads live stock while a sheet sits open, or whether stock is frozen at sheet creation. No mention of a cut-off, a freeze, a lock, or a "stock changed since you started" warning anywhere in the workflow article. The doc does say the sheet auto-saves server-side on blur, but says nothing about the system-quantity column's refresh behaviour. **This is a documentation silence, not a negative finding — do not state either behaviour as fact.**
- **Multi-user parallel counting: undocumented, with weak contrary signal.** No page describes two people or two devices counting one sheet simultaneously, any conflict resolution, or any per-counter attribution of lines. The only counter field is a single **"Nhân viên kiểm"** per sheet, which points away from parallel counting — but the docs never state it is prohibited.
- **Offline behaviour: undocumented.** Zero mentions of offline, sync-on-reconnect, or queued counts in the Kiểm kho app articles or the app-store listing. (Note: Sapo documents an offline mode for the **POS** channel — `chuyen-che-do-ban-tu-online-sang-offline-tren-kenh-ban-hang-pos` — but nothing equivalent for Kiểm kho. Do not transfer the POS behaviour to stocktaking.)
- **No Sapo Pharma help documentation exists to find.** Searched the help centre product switcher and article index; pharmacy exists only as (a) a business-field setting, (b) the `lien-thong-nha-thuoc` article, and (c) generic lô-HSD articles. The premise that a richer pharma stocktaking variant exists is **false as far as published docs go**.
- **Recording a newly found lot (zero system stock):** not documented as possible. The workflow describes **"Chọn lô kiểm"** — choosing from existing lots — and the partial-count prompt only offers to zero or preserve *known* lots. **No documented path to create a lot during a count.** Consistent with round 1. Stated as undocumented, not as a proven prohibition.
- **Serial-managed products in OmniAI kiểm kho:** the mobile exclusion list names *dịch vụ, lô, combo* but not serial. Round 1's serial exclusion could not be re-confirmed for the OmniAI app in this run.
- **Any effective/updated date on pricing.** `www.sapo.vn/bang-gia.html` carries no "áp dụng từ" date and no last-updated stamp. Help articles carry no publication dates either; the only temporal marker anywhere is the footer **"Copyright © 2026"**. Treat all freshness as "live as of 2026-09-21" with no provenance depth.
- **`help.sapo.vn/search?query=...` is not usable for research** — it returns only the sidebar navigation, no result rows (likely JS-rendered). Candidate URLs `help.sapo.vn/kiem-hang`, `/tao-phieu-kiem-hang`, `/huong-dan-kiem-hang`, `/kiem-hang-theo-lo` all fail to resolve. Discovery has to go through the per-product "Tổng quan" hub pages.
- **No Sapo community/forum content was located.** No official forum surfaced; blog posts on sapo.vn are marketing register and were not used as evidence.
