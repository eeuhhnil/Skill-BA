# KiotViet — kiểm kho, round 2

Accessed 2026-09-21. 8 sources fetched this run. All claims below trace to a page retrieved in this run.

## Findings

### Gap 1 — hotro.kiotviet.vn

- **`hotro.kiotviet.vn` is NOT a help centre. It is the authenticated app/support shell (an SPA that renders unresolved i18n placeholders such as `{{_l.sale_Cashier}}` to an anonymous fetcher). It contains no kiểm kho articles.** The real, public help centre is `kiotviet.vn/huong-dan-su-dung-kiotviet/…`.
  - source: https://hotro.kiotviet.vn/ · publisher: KiotViet (Citigo) · pub_date: none · accessed: 2026-09-21 · confidence: high · class: feature
  - Round 1's 503 was transient; the retry succeeded and the lead is dead. Do not spend further budget there.
- Note: the help-centre category URL `…/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/` returns **404** — that older URL family is retired. Live articles sit under `retail-hang-hoa/`, `retail-chuyen-nganh/`, `huong-dan-bar-cafe-nha-hang/`, `salon-hang-hoa/`, `ung-dung-tren-mobile-mobile-app/`.

### Gap 2 — vertical diff

- **ROUND 1 CORRECTION: gộp phiếu (merging count sheets) is NOT F&B-unique. It is in the core retail guide and in the mobile app guide too.** Retail: *"Gộp nhiều phiếu kiểm kho tạm"* — *"tích chọn các phiếu ở trạng thái Lưu tạm cần gộp → nhấn nút Gộp phiếu"*, *"hệ thống tạo một phiếu tạm mới với số lượng thực tế được cộng dồn từ các phiếu đã chọn"*.
  - source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/kiem-kho/ · publisher: KiotViet · pub_date: none shown · accessed: 2026-09-21 · confidence: high · class: feature · vertical: **retail (bán lẻ)**
  - corroborated: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/ung-dung-tren-mobile-mobile-app/kiem-kho-retail/ (same "cộng dồn" wording) · confidence: high · vertical: **mobile app**
- **Multi-user parallel counting is an explicitly documented use case, and the unit of parallelism is the physical area/zone.** F&B guide, verbatim: *"Khi có nhiều người kiểm kho ở nhiều khu vực trong kho hàng, sẽ có nhiều phiếu kiểm kho tương ứng"* — then merge. Retail guide frames the same as *"nhiều nhân viên cùng kiểm kho ở các khu vực khác nhau"*.
  - source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-bar-cafe-nha-hang/kiem-kho/ · publisher: KiotViet · pub_date: page states last update **2022-02-13** (stale — downgrade) · accessed: 2026-09-21 · confidence: high · class: feature · vertical: **F&B**
  - Important nuance: this is **merge-after, not concurrent editing of one sheet**. Each counter makes their *own* phiếu tạm; the merge sums the Thực tế columns and deletes the originals. There is no documented locking, assignment, or per-zone section inside a single sheet. "Counting by area" exists only as this convention, not as a modelled zone/location field.
- **Four tabs on the count sheet: `Tất cả` / `Khớp` (thực tế = tồn) / `Lệch` / `Chưa kiểm`.** Documented in the F&B guide; the retail page did not enumerate them in the fetched text but the feature is the same grid.
  - source: F&B guide URL above · confidence: high · class: feature · vertical: **F&B (explicit), retail (implied)**
- **Pharmacy is the one genuinely differentiated vertical, and the difference is regulatory (Liên thông CSDL Dược), not counting mechanics.** Verbatim: *"Phiếu kiểm đã cân bằng kho có chứa thuốc đã liên thông sẽ tự động đồng bộ lên CSDL Dược."* And a hard operational rule: *"Khi lập phiếu kiểm kho, không nên tạo lô mới"* — new lots must first be declared via a purchase receipt (phiếu nhập), otherwise the national Pharmacy Database rejects the sync.
  - source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-chuyen-nganh/nganh-nha-thuoc/ · publisher: KiotViet · pub_date: **2026-08-29** (fresh) · accessed: 2026-09-21 · confidence: high · class: feature · vertical: **nhà thuốc / pharmacy**
  - So: pharmacy lô/HSD counting is not *better* than the generic lô/HSD count — it is the same mechanic plus a downstream government sync and a constraint that makes a count sheet a **bad** place to discover an undeclared lot.
- **Lô/HSD counting is line-per-lot: when building the sheet you pick each lot and enter that lot's actual quantity.** Consistent with round 1.
  - source: search-surfaced KiotViet help text for https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/hang-hoa-lo-han-su-dung/ · publisher: KiotViet · pub_date: none · accessed: 2026-09-21 · confidence: **medium** (read via search result summary, page not fetched directly) · class: feature · vertical: retail + pharmacy
- **Thời trang (fashion): no dedicated kiểm kho help article found.** The fashion material located is a marketing page (`/kho-hang-thoi-trang/`), not documentation. Treat fashion as using the standard retail kiểm kho.
  - confidence: medium (absence of evidence) · class: feature
- **Salon vertical has its own kiểm kho article** with an identical mechanic (add items by search / barcode / category / Excel import, enter Thực tế, system computes the difference, one-click cân bằng kho). No merging or lot content surfaced for salon.
  - source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/salon-hang-hoa/kiem-kho/ (read via search result summary, not fetched directly) · pub_date: none · confidence: medium · class: feature · vertical: **salon**

### Gap 3 — the two open questions

- **Snapshot / cut-off: THE DOCUMENTATION IS SILENT. This is the finding.** Four KiotViet help pages were read specifically for this (retail kiểm kho, F&B kiểm kho, mobile kiểm kho, "Thay đổi nội dung phiếu kiểm kho"). **None** states whether the Tồn kho column is a snapshot taken at sheet creation or re-read live at cân bằng kho; none mentions freezing stock; and **no page carries any warning against selling while a count sheet is open.** There is no "cut-off", "chốt", or "tạm khóa kho" concept anywhere in the fetched material.
  - sources: retail / F&B / mobile kiểm kho URLs above + https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/thay-doi-noi-dung-phieu-kiem-kho/ · accessed: 2026-09-21 · confidence: high (that the docs are silent) · class: feature
  - Do not infer the behaviour. The only documented adjacent fact is that a phiếu tạm can be saved and resumed later (*"Lưu tạm"*), which makes the snapshot question operationally sharp but does not answer it.
- **Uncounted items on cân bằng kho: ALSO UNDOCUMENTED.** The `Chưa kiểm` tab is documented as a *filter*. No fetched page says what happens to items left in `Chưa kiểm` when the sheet is finalised — neither "set to zero" nor "left unchanged" appears. Round 1's gap stands after a second honest attempt.
  - confidence: high (that the docs are silent) · class: feature
  - Weak indirect signal, offered as belief not fact: the retail guide's finalisation wording is *"cập nhật lại số lượng tồn kho về đúng bằng số lượng thực tế"* (update stock to equal the **actual** figure). If an uncounted row has no Thực tế value at all, that sentence does not define an outcome for it. **Unverified.**

### Gap 4 — pricing, now dated

- **A dated price-increase announcement exists. Published 2025-04-24, effective 2025-05-01: Gói Hỗ trợ 250.000đ/tháng, Gói Chuyên nghiệp 310.000đ/tháng, Gói Cao cấp 490.000đ/tháng. Direction: increase ("điều chỉnh giá", framed as market-driven). The announcement does not print the pre-May-2025 prices, so the magnitude of that increase is not establishable from it.**
  - source: https://www.kiotviet.vn/kiotviet-thong-bao-dieu-chinh-gia-ban-san-pham-phan-mem-quan-ly-ban-hang/ · publisher: KiotViet · pub_date: 2025-04-24 · accessed: 2026-09-21 · confidence: high · class: pricing
- **Therefore prices rose a SECOND time between 2025-05-01 and today: 250k → 270k and 310k → 330k, while 490k held flat.** The live `/phi-dich-vu` page today shows 270.000đ / 330.000đ / 490.000đ. No announcement for this second move was found, and **`/phi-dich-vu` still carries no effective date.** web.archive.org is blocked from this environment, so the exact date of the 270/330 move could not be pinned.
  - source: https://www.kiotviet.vn/phi-dich-vu/ · publisher: KiotViet · pub_date: none shown · accessed: 2026-09-21 · confidence: high (on the numbers), medium (on the inference that this is a distinct second increase) · class: pricing
- **Metering, confirmed on the live price page.** Extra warehouse: **150k / +1 kho / month**, on both Chuyên nghiệp and Cao cấp. Extra branch is metered *differently by tier*: **270k/+1 chi nhánh** on Chuyên nghiệp vs **375k/+1 chi nhánh** on Cao cấp. Users: Hỗ trợ caps at **3 accounts**; Chuyên nghiệp and Cao cấp are unlimited accounts. E-invoice and digital signature are listed **Miễn phí** (free) on all packages.
  - source: https://www.kiotviet.vn/phi-dich-vu/ · accessed: 2026-09-21 · confidence: high · class: pricing
- **Mobile kiểm kho is not metered as an add-on.** The `/phi-dich-vu` page lists no mobile line item and the mobile kiểm kho help page presents the feature as a standard function, not a paid extra. Mobile kiểm kho was launched as a product announcement (`/kiotviet-ra-mat-tinh-nang-kiem-kho-va-them-moi-hang-hoa-tren-di-dong/`, not fetched this run).
  - confidence: medium (absence of a price line is not the same as a stated inclusion) · class: pricing
- Same 270/330/490 ladder applies to bán lẻ, F&B and health & beauty. **Lưu trú (accommodation) is a different ladder: 220k (1–15 phòng) / 490k (16–30 phòng) / 990k (unlimited)**, metered by room count, extra branch 375k or 750k.
  - source: https://www.kiotviet.vn/phi-dich-vu/ · confidence: high · class: pricing

## Leads

- `https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/hang-hoa-lo-han-su-dung/` — fetch directly; likely the definitive lot-counting mechanic, upgrading a medium-confidence finding.
- `https://www.kiotviet.vn/kiotviet-ra-mat-tinh-nang-kiem-kho-va-them-moi-hang-hoa-tren-di-dong/` — dated launch announcement for mobile kiểm kho; would date that capability.
- `https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/salon-hang-hoa/kiem-kho/` and the fashion vertical — fetch directly to close the vertical diff properly.
- A retired-URL sweep: `/huong-dan-kiem-kho/…` 404s at the category level but the *child* article `thay-doi-noi-dung-phieu-kiem-kho/` still resolves. There may be other orphaned children under that prefix carrying the Chưa kiểm / snapshot answers.
- The snapshot and Chưa kiểm questions will likely only be settled by a trial account or a support-ticket answer, not by published docs. Recommend closing them as "undocumented" for the teardown rather than spending more research budget.
- No announcement found for the 250→270 / 310→330 move. A Vietnamese-language news/forum search, or a KiotViet Facebook post search, is the remaining route; web.archive.org is unavailable from this environment.

## Looked for but could not find

- **Any statement of whether Tồn kho is frozen, snapshotted, or live during an open phiếu tạm.** Searched 4 KiotViet help pages. Zero occurrences of any cut-off concept. Genuinely silent.
- **Any warning telling users not to sell during a stocktake.** None exists in KiotViet's own docs.
- **What happens to `Chưa kiểm` items at cân bằng kho.** The tab is documented; its finalisation semantics are not. Silent.
- **Any dated announcement for the current 270k/330k/490k prices.** Only the 2025-05-01 announcement (250/310/490) was found. The live price page remains undated.
- **A dedicated thời trang (fashion) kiểm kho help article.** Only marketing pages surfaced.
- **Any concurrent/locked multi-user editing of a single count sheet, or a modelled zone/location field.** KiotViet's answer is one-sheet-per-counter plus post-hoc merge. No evidence of anything stronger.
- **Any cycle-counting / partial-count scheduling feature** (recurring counts, ABC classes, count-by-cycle). No mention in any vertical. The only partiality is manual: build a sheet containing a subset of goods.
- **A separate approval/review step before cân bằng kho.** Round 1's finding stands — nothing found this run contradicts it.
- **hotro.kiotviet.vn as a content source.** It is an app, not a knowledge base. Lead closed.
