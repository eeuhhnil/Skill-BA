# Sapo — kiểm kê kho (stocktaking) teardown — round 1, pass 1

Accessed: 2026-09-21. Budget spent: 15 tool calls, 5 sources actually read (4 vendor pages + 1 vendor app-store listing), 3 web searches.

Important context on the source estate: `support.sapo.vn/*` now 301-redirects to `help.sapo.vn/*`; `hotro.sapo.vn` returns 403. The current-generation product is branded **Sapo OmniAI** and the stocktake feature ships as an installable app called **"Kiểm kho"** from `apps.sapo.vn`. There appear to be at least two distinct stocktake implementations — the retail/Omni one (Sản phẩm > Kiểm hàng, "phiếu kiểm hàng") and the **Sapo FnB** one (Kho hàng > Kiểm kê kho, "phiếu kiểm") — with different UI vocabulary and different statuses. Findings are tagged by variant.

---

## Findings

### A. Feature teardown

- {claim: "Retail/Omni flow is: **Sản phẩm > Kiểm hàng > Tạo phiếu kiểm** → choose branch (chi nhánh) → assign counting staff (defaults to logged-in user) → sheet code auto-generated if blank → add products → enter counted qty → click **Cân bằng kho** to finalise. There is no separate 'submit for approval' step between counting and stock adjustment.", source URL: https://help.sapo.vn/tao-phieu-hkiem-hang-thu-cong-tren-phan-mem-sapo, publisher: Sapo (help.sapo.vn), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}
  - NOTE: correct URL is https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo (typo guard — this is the page actually fetched).

- {claim: "**Blind counting is NOT the default — and appears unavailable.** The retail counting grid shows four parallel columns: **Tồn chi nhánh** (system on-hand), **Tồn thực tế** (counted, user input), **Lệch** (auto-computed variance), **Lý do** (reason, optional), **Ghi chú** (note). The counter sees the system number next to the input box.", source URL: https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "Sapo FnB likewise shows the system figure: the line label is **'Số lượng ban đầu (hiện tại)'** — i.e. the system quantity at the moment the sheet is created — and variance = initial minus counted.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "**Snapshot / cut-off: no freeze.** The FnB doc's phrasing 'Số lượng ban đầu (hiện tại)' reads as a point-in-time capture at sheet creation, and neither the FnB nor the retail article describes any locking of stock, blocking of sales, or re-basing of the system column while a sheet is open. This is inference from labelling plus absence, not an explicit statement.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: **low**, class: feature}

- {claim: "**Document statuses, retail/Omni (3): 'Đang kiểm kho' → 'Đã cân bằng' → 'Đã xóa'.** The list view also tracks **'Ngày cân bằng'** (balancing date), distinct from creation date.", source URL: https://help.sapo.vn/xem-danh-sach-phieu-kiem-hang, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "**Document statuses, Sapo FnB (2): 'Chưa cân bằng'** (draft, editable) **→ 'Đã cân bằng'** (finalised, inventory adjusted to counted amounts, no further editing). FnB therefore has an explicit 'finalised sheets are locked' rule that the retail doc does not state.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "**Batch/lô IS supported in retail Sapo, with two hard constraints.** Verbatim: *'Sản phẩm quản lý theo lô cần chọn đúng lô trước khi nhập số lượng'* — you must pick the specific lot before entering a quantity, so counting is per-lot, not per-SKU, for lot-managed goods. Only lots with on-hand > 0 can be counted — **you cannot count a lot into existence via stocktake**, which is a real gap for found/unrecorded stock. And if a stocktake drives a lot to zero, *'giá vốn của lô đó sẽ về 0'* (that lot's cost price resets to zero) — a costing landmine.", source URL: https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "**Serial-managed products are explicitly excluded from stocktaking**: *'Sản phẩm quản lý theo Serial chưa hỗ trợ tính năng kiểm hàng.'* ('chưa' = not yet.)", source URL: https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "Input methods, retail: search by product name / SKU / **barcode**; **'Chọn nhiều'** for bulk multi-select; **'Thêm nhanh sản phẩm'** to add a whole set by filter criteria (this is the mechanism for cycle/partial counting by category). Excel import is referenced on the page but with no documented preview, validation-rule, or error-handling step for stocktake specifically — the only error-code article linked is for customer-file import, not stocktake.", source URL: https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "The **'Kiểm kho' app is free**, is exclusively for **Sapo OmniAI** (explicitly not compatible with older Sapo versions), is **web-based**, supports **up to 10,000 items per sheet**, supports **wired barcode scanners or the smartphone camera** as scanner, does automatic stock balancing, and has file import. No reviews or ratings are published on the listing.", source URL: https://apps.sapo.vn/stock-take, publisher: Sapo Technology JSC (apps.sapo.vn), pub_date: undated/no last-updated stamp, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "**Permissions exist but are coarse and do not separate counting from adjusting.** The documented permissions are **'Xem danh sách kiểm hàng'** (view stocktake list) and **'Tạo phiếu kiểm hàng'** (create stocktake sheet). No 'approve' or 'balance stock' permission is documented — whoever can create a sheet appears able to press Cân bằng kho and move real stock.", source URL: https://help.sapo.vn/tao-phieu-kiem-hang-thu-cong-tren-phan-mem-sapo + https://help.sapo.vn/xem-danh-sach-phieu-kiem-hang, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "**Variance is quantity-only.** Neither the retail nor the FnB article shows a monetary variance / value-of-loss column. FnB computes variance = initial − counted and captures a free-text reason; no cost impact is surfaced.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "**Sapo FnB counts both 'nguyên liệu' (ingredients) and 'mặt hàng' (items) in the same sheet**, selected manually via a search dialog with checkboxes; each line shows the material/item's unit. **No Excel import for FnB stocktake is documented**, and no unit-conversion logic is documented in either variant.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "**Scope is opt-in, not whole-warehouse.** In both variants the user explicitly picks which products/materials go on the sheet; nothing in the docs describes a 'count everything in this warehouse' sheet that auto-populates the full catalogue. This makes partial/cycle counting the native mode and makes the 'uncounted items' question partly moot for items never added — but leaves open what happens to items added to the sheet and left blank.", source URL: https://help.sapo.vn/tao-phieu-kiem-ke-kho-nguyen-lieu-mat-hang-tren-trang-quan-tri-sapo-fnb, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

### B. Packaging / tier gating

- {claim: "The 'Kiểm kho' app itself is **free** but gated on being on **Sapo OmniAI**. Stocktaking is thus not a paid add-on; the gate is the platform generation, not the price tier.", source URL: https://apps.sapo.vn/stock-take, publisher: Sapo, pub_date: undated, accessed: 2026-09-21, confidence: high, class: pricing}

- {claim: "Published Sapo retail pricing (as surfaced from www.sapo.vn/bang-gia.html): **Start Up 249,000 VND/month** on a 1-year term, falling to **170,000 VND/month** on 2+ year terms (up to ~31% off); **Retail Pro 249,000 VND/month** on 2+ year terms; **Omnichannel 599,000 VND/month**. 7-day free trial. Setup fee waived for new retail/web customers.", source URL: https://www.sapo.vn/bang-gia.html, publisher: Sapo, pub_date: undated (no visible 'cập nhật' stamp captured), accessed: 2026-09-21, confidence: **low-medium**, class: pricing}
  - **Caveat, read this:** these figures came from a search-engine synthesis of that page, **not from a direct fetch I performed** — `https://www.sapo.vn/bang-gia` (no `.html`) returned 404 and I ran out of budget before retrying with the `.html` suffix. Treat as unverified until `https://www.sapo.vn/bang-gia.html` is fetched directly. I also could not map which tier contains kiểm hàng.

### C. Customers' voice

- {claim: "Aggregated Vietnamese review/comparison content lists Sapo's weaknesses as: no warranty-management (bảo hành) feature; feature overload on Omnichannel/Growth tiers ('gây ngợp cho người mới'); weak post-sale support/training with hotline congestion at peak hours; limited customisation; and complexity in multi-channel shipping/order management. **None of this is stocktake-specific.**", source URL: search synthesis over https://tino.vn/blog/phan-mem-sapo-la-gi/, https://fastdo.vn/phan-mem-ban-hang-sapo/, https://www.pos365.com.vn/2023/07/danh-gia-phan-mem-sapo-co-tot-khong.html, publisher: various (Tino, Fastdo, POS365), pub_date: 2023–2026, accessed: 2026-09-21, confidence: **low**, class: sentiment}
  - Red flags: POS365 and KiotViet are **direct competitors publishing "reviews" of Sapo** — treat as adversarial marketing. tino.vn and fastdo.vn are affiliate/SEO blogs. No first-party review platform (G2/Capterra equivalent), no Facebook group thread, and no 1–3★ review was reached this run.

---

## Leads

1. **Fetch `https://www.sapo.vn/bang-gia.html` directly** — the `.html` suffix is the live path; my 404 was a URL-shape miss, not an absent page. Highest-value single next call.
2. **`https://help.sapo.vn/ung-dung-kiem-kho`** — fetched but the article body came back truncated behind the nav chrome. This is *the* canonical page for the Kiểm kho app and very likely contains the snapshot/cut-off, blind-count and multi-user answers. Retry, possibly via a different prompt or a cached/AMP variant.
3. **Contradiction to resolve:** retail/Omni has 3 statuses (Đang kiểm kho / Đã cân bằng / Đã xóa) while FnB has 2 (Chưa cân bằng / Đã cân bằng). FnB explicitly locks balanced sheets; retail docs are silent. Two different engines, or one doc simply less complete? Materially affects any "can a finalised sheet be edited" claim.
4. **Two more Sapo variants unexamined:** Sapo Pharma / nhà thuốc (should have the strongest lô + hạn sử dụng handling, given Vietnamese pharmacy regulation) and the Sapo mobile POS app. Neither was reached. Search `help.sapo.vn` for "nhà thuốc kiểm kê".
5. **The lot cost-reset behaviour** (*'giá vốn của lô đó sẽ về 0'*) is a genuine, quotable defect surface — worth checking whether Sapo has since patched it, and worth probing in user forums as a complaint vector.
6. **Serial-number stocktaking is unsupported ('chưa hỗ trợ')** — a clean wedge for any competitor serving electronics/IMEI retail.
7. **Excel-import validation for stocktake** is undocumented and the only error-code article Sapo links is for *customer* import. Likely thin or absent — probe for a dedicated import-preview article.
8. **No changelog found.** Sapo appears not to publish a public product changelog/release-notes feed; `sapo.vn/blog` carries pricing-change announcements (`/blog/thay-doi-bang-gia-phan-mem-quan-ly-ban-hang-sapo`, `/blog/thong-bao-thoi-gian-thay-doi-bang-gia-...`) but these are commercial, not product. Worth one targeted look for "Sapo cập nhật tính năng" before concluding there is none.
9. **Sentiment is a hole.** Try: Google Play / App Store reviews of the Sapo POS mobile app (rich 1–3★ source, date-stamped), and Vietnamese Facebook seller groups. Competitor-authored "reviews" should be excluded.

---

## Looked for but could not find

- **SNAPSHOT / CUT-OFF BEHAVIOUR — NOT ESTABLISHED.** This was the brief's single most important question and I did not answer it. No Sapo document I read states whether the system-quantity column on an open sheet is a frozen snapshot or a live figure, nor what happens when a POS sale decrements stock mid-count, nor whether any freeze/lock exists. My weak inference (no freeze; snapshot taken at creation) rests on the FnB label *'Số lượng ban đầu (hiện tại)'* and on silence elsewhere. **Absence of any freeze concept in the docs is itself weak evidence that none exists** — a stock-freeze feature is the kind of thing a vendor documents loudly — but this must be confirmed by trial account or by `help.sapo.vn/ung-dung-kiem-kho`.
- **UNFINISHED / UNCOUNTED ITEMS — NOT ESTABLISHED.** Neither variant's documentation says what Cân bằng kho does with a line that is on the sheet but has an empty 'Tồn thực tế'. Zeroed, skipped, or blocked? Unknown. Both docs are silent, and this is a high-consequence ambiguity (an accidental zeroing would wipe stock).
- **Multi-user parallel counting on one sheet** — not mentioned anywhere I read. Retail assigns a single "nhân viên kiểm" defaulting to the logged-in user, which hints at single-assignee sheets, but that is a hint, not a finding.
- **Unit conversion (thùng/lốc/cái) during counting** — no coverage in either variant. FnB shows one fixed unit per line.
- **Monetary variance** — no evidence it exists; no evidence it doesn't beyond absence in two docs.
- **Whether a retail 'Đã cân bằng' sheet can be edited, reopened, or reversed** — retail doc silent (FnB says no).
- **Any approval workflow** — none documented in either variant; I found no "chờ duyệt" status anywhere.
- **Excel import preview/validation step for stocktake** — not documented.
- **A native mobile counting app** — the Kiểm kho app is described as web-based using the phone camera as a scanner, not as a native offline counting app. No offline-counting capability found.
- **Public changelog / release notes for inventory features** — none located.
- **Sapo Pharma / nhà thuốc stocktake behaviour** — not reached at all; every batch/expiry finding above is retail-variant.
- **First-party or neutral user reviews with star ratings and dates** — none reached. All sentiment material found was competitor- or affiliate-authored.
- `hotro.sapo.vn` returned **403 Forbidden**; `support.sapo.vn` is fully retired into `help.sapo.vn`.
