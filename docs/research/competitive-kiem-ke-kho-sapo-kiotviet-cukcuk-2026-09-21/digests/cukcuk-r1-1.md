# CukCuk (MISA) — kiểm kê kho — Round 1, pass 1

Accessed: 2026-09-21. Budget spent: 14 web tool calls, 6 distinct sources read.

Sources actually read this run:
1. https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho (official help, current)
2. https://trienkhai.cukcuk.vn/1010200_kiem_ke_kho.htm (official deployment/help mirror of same article)
3. https://www.cukcuk.vn/bang-gia/ (vendor pricing page)
4. https://helpv2.cukcuk.vn/vi/kb/r68_vn (official release note R68)
5. https://helpv2.cukcuk.vn/vi/ac/tinh_nang_moi_table_service ("Tính năng mới" changelog archive)
6. https://helpv2.cukcuk.vn/vi/kb/1060300_them_nvl (official help — khai báo nguyên vật liệu)

---

## Findings

### Feature — end-to-end flow

- **claim:** The stocktaking flow is: `Nghiệp vụ Kho > Kiểm kê kho > Thêm` → declare sheet header → enter counted quantities → `Cất` (save) → `Xử lý` (process). It is a two-stage document: saving and processing are separate actions.
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho · publisher: MISA (CUKCUK official help) · pub_date: not shown on page · accessed: 2026-09-21 · confidence: high · class: feature

- **claim:** Variance is not adjusted in place. On `Xử lý`, the system auto-generates warehouse documents for the difference: surplus → a **Nhập kho kiểm kê** (goods-receipt), shortage → a **Xuất kho kiểm kê** (goods-issue). Verbatim: *"hệ thống sẽ tự động sinh phiếu xuất kho/nhập kho tương ứng với lượng nguyên vật liệu chênh lệch thừa/thiếu"*. These land in the Nhập/Xuất tabs of the Kho module.
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho + https://trienkhai.cukcuk.vn/1010200_kiem_ke_kho.htm · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high · class: feature
  - **Wedge note:** this means the audit trail is "count sheet + generated adjustment document", i.e. the adjustment is a normal inventory movement, not a special reconciliation posting.

- **claim:** The sheet records a **reason per line** (`Nguyên nhân`) alongside the counted quantity — these are the only two columns the Excel import actually consumes.
  - source: https://trienkhai.cukcuk.vn/1010200_kiem_ke_kho.htm · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high · class: feature

- **claim:** There is a **"Thành viên tham gia"** tab to record the staff who took part in the count. (People-on-the-count is modelled; approval is not — see gaps.)
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high · class: feature

### Feature — what is counted

- **claim:** Stocktaking is over **nguyên vật liệu (raw materials/ingredients)**, not finished dishes/retail SKUs. The help article speaks throughout of "danh sách NVL" and "lượng nguyên vật liệu chênh lệch"; the master-data article `Khai báo nguyên vật liệu` likewise covers only NVL.
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho + https://helpv2.cukcuk.vn/vi/kb/1060300_them_nvl · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high · class: feature
  - **This is the model difference to flag:** CukCuk counts the kitchen store (ingredient layer). Consumption reaches that layer through recipes (định lượng), so a count variance is "theoretical recipe consumption vs. reality" — a yield/waste/theft number — not a retail SKU shrink number.

- **claim:** Stocktaking can be done **by quantity and by value** (`số lượng` and `giá trị`). Unit prices are pre-filled from recent warehouse transactions and remain **editable** on the sheet — so the variance carries a monetary amount, not only a quantity.
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high · class: feature

- **claim:** Value-based stocktaking is a **later addition**, not original. Release note R68 states the requirement verbatim: *"QLNH/Kế toán muốn kiểm kê lại nguyên vật liệu theo cả số lượng và giá trị để cân lại kho (Hiện tại chỉ kiểm kê được theo số lượng)"* — i.e. before R68 only quantity counting existed.
  - source: https://helpv2.cukcuk.vn/vi/kb/r68_vn · publisher: MISA · pub_date: page rendered a date of 25/12/2025, which I do not trust (R108 is dated 22-06-2023, so R68 must be far older — likely ~2017–2018; the rendered date is probably a page-update stamp) · accessed: 2026-09-21 · confidence: high on the content, **low on the date** · class: feature

### Feature — input methods

- **claim:** Two input paths only: (a) type counts directly into the kiểm kê screen, (b) **export the NVL list to an Excel template, count offline, import the file back**. No barcode scanning and no mobile counting app is mentioned anywhere in the stocktaking documentation.
  - source: https://helpv2.cukcuk.vn/vi/kb/1010200_kiem_ke_kho + https://trienkhai.cukcuk.vn/1010200_kiem_ke_kho.htm · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high for the two documented paths; medium for the absence of barcode/mobile (absence in docs, not a vendor denial) · class: feature

- **claim:** Unit conversion exists at the **master-data** level: an NVL has `Đơn vị tính` (primary unit) plus `Đơn vị chuyển đổi` with `tỉ lệ chuyển đổi` and an "Là đơn vị bán" flag. Whether the count sheet lets you enter in a conversion unit is **not stated**.
  - source: https://helpv2.cukcuk.vn/vi/kb/1060300_them_nvl · publisher: MISA · pub_date: not shown · accessed: 2026-09-21 · confidence: high (existence of conversion units) / low (use during counting) · class: feature

### Pricing / tier gating

- **claim:** Inventory (`quản lý kho`) — and therefore stocktaking — is **gated above the base tier**. Published tiers: **STANDARD 199.000đ/tháng** (sales, menu, staff, promotions, table ordering; 12 reports) — no inventory; **PROFESSIONAL 299.000đ/tháng** (adds thu chi, mua hàng, **kho**, công nợ; 48 reports); **ENTERPRISE 499.000đ/tháng** (Professional + MISA Lomas CRM). Each extra location costs the same as the tier. 15-day free trial; no setup fee stated. CukCuk Web add-on 1.500.000đ/năm.
  - source: https://www.cukcuk.vn/bang-gia/ · publisher: MISA · pub_date: **no published date on the page** · accessed: 2026-09-21 · confidence: high on the numbers as currently published, medium on freshness (undated vendor page) · class: pricing

- **claim (unverified, from search snippet only — did not fetch):** MISA advertises a free-for-life CukCuk tier for individual business households with revenue ≤ 1 tỷ đồng/năm. Treat as a lead, not a finding.
  - source: search result snippet, publisher MISA · confidence: low · class: pricing

---

## Leads

- **R68 dating problem.** helpv2 renders R68 with 25/12/2025 while R108 is separately dated 22-06-2023. The help site's dates are unreliable; verify any changelog date against a second source before relying on it.
- **Changelog archive is live and worth a dedicated pass.** https://helpv2.cukcuk.vn/vi/ac/tinh_nang_moi_table_service currently lists R158, R157, R156, R155, R149 Mobile, R148, R147, R145, R144, R143 Mobile (R143 Mobile dated 05-02-2026). Listing entries are truncated, so per-version pages (e.g. `helpv2.cukcuk.vn/vi/kb/r158`) must be opened individually to find inventory items. **No inventory/stocktaking item was visible in the archive listing text** — weak signal that stocktaking is not an active investment area, but not proof.
- **Mobile releases are a separate track** ("R149 Mobile", "R143 Mobile"). Whether any mobile release added counting on the phone app is unchecked; `helpv2.cukcuk.vn/vi/kb/nhap-kho` documents *goods receipt* on the CUKCUK Bán hàng phone app, which proves warehouse operations exist on mobile — so a mobile kiểm kê screen is plausible and worth one targeted fetch.
- **Related warehouse docs not yet read**, each likely to contain mechanics the kiểm kê page omits: `1010300_chuyen_kho` (transfer), `1010300_nhap_kho`, `1010100_nhap_xuat_ton_kho`, `1050000_tinh_hinh_ton_kho` (stock-on-hand report — likely reveals whether tồn kho is computed live).
- **Accounting hand-off:** `helpsme.misa.vn/2026/kb/kiem-tra-va-ghi-so-chung-tu-nhap-xuat-chuyen-kho-lay-ve-tu-cukcuk/` shows MISA SME 2026 pulls CukCuk's nhập/xuất/chuyển kho documents and posts them (`ghi sổ`). Notably the title lists nhập/xuất/**chuyển** kho — not kiểm kê — but since kiểm kê emits a nhập/xuất document, the adjustment presumably flows through. Worth confirming; it is a real differentiator story (count → accounting posting).
- **Contradiction to resolve:** vendor marketing (cukcuk.vn blog pages) claims automatic ingredient deduction by định lượng and minimum-stock alerts, but the primary NVL help article does not state either. Marketing-vs-docs gap; needs a primary doc on định lượng/công thức.
- **Batch/expiry gap is a candidate wedge.** A MISA-side article surfaced in search noted that basic warehouse software often "lacks management by location or batch number" — and CukCuk's own NVL master-data page has no lô/hạn sử dụng field. If confirmed, CukCuk cannot count by batch at all.

---

## Looked for but could not find

Stated plainly — these are real gaps in the evidence, not omissions in my search:

- **Snapshot / cut-off behaviour: NOT ESTABLISHED.** I asked the primary help article directly and it is silent. There is no documented concept of freezing stock at a point in time, no mention of a cut-off timestamp on the sheet, and nothing about what happens to the system quantity when POS sales deplete ingredients while a count sheet is open and saved but not yet `Xử lý`. Given the design (variance is materialised as a generated nhập/xuất document at `Xử lý` time), the likely behaviour is that the comparison happens at processing time against then-current stock — but **that is inference, not evidence.** Flag as unknown.
- **Blind counting: NOT ESTABLISHED.** The documentation describes entering "số lượng kiểm kê thực tế" but never says whether the book/system quantity is displayed next to the input. Since the Excel export ships the NVL list to the counter, the offline path at minimum is not blind unless the template omits the quantity column — undetermined.
- **Unfinished items: NOT ESTABLISHED.** No statement about what happens to materials on the sheet left blank / never counted when `Xử lý` runs (zeroed vs. left unchanged vs. excluded). This is exactly the destructive-edge-case question and the docs do not answer it.
- **Document statuses: NOT DOCUMENTED.** No status vocabulary (Chưa xử lý / Đã xử lý / Ghi sổ / Hủy) appears in the help article. Only the actions `Cất` and `Xử lý` are named. Whether a processed sheet can be edited, deleted or reversed is also not stated.
- **Approval step / permission separation:** nothing found. No mention of phân quyền for kiểm kê, and no approval state between counting and stock adjustment. The "Thành viên tham gia" tab is record-keeping, not an approval workflow.
- **Batch / expiry (lô, hạn sử dụng) counting:** no evidence it exists. Not in the count sheet docs, not a field on the NVL master record.
- **Barcode scanning during count:** no evidence. Not mentioned in any read page.
- **Excel import preview/validation:** not documented. Only that the template's `Kiểm kê` and `Nguyên nhân` columns are read on import; no mention of a validation/preview step or error report.
- **Mobile counting:** not documented for kiểm kê (goods receipt on the phone app is documented, counting is not).
- **Recent changelog entries touching stocktaking:** none found in the visible "Tính năng mới" archive (R143–R158 window). The only stocktaking changelog item I located is the old R68 quantity+value change.
- **Customer voice (Section C): essentially empty — report as thin.** Two searches for Vietnamese user complaints/reviews about CukCuk inventory returned almost entirely CukCuk's own marketing blog and MISA-owned properties (amis.misa.vn, sme.misa.vn), plus one competitor's SEO page (pos365.vn). **I found zero first-hand user reviews, forum threads or Facebook-group discussions about CukCuk stocktaking in this run.** The web search tool's US-centric index is the likely cause. Next round should go at forum.misa.vn directly (it surfaced and is a real user forum), Google Play / App Store reviews for the CUKCUK apps, and Vietnamese review aggregators — none of which I reached within budget. Do not treat the absence as evidence that users are satisfied.
