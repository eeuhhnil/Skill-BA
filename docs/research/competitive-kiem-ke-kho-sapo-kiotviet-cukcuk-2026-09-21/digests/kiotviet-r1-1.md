# KiotViet — Kiểm kê kho (stocktaking) teardown — round 1, pass 1

Accessed: 2026-09-21. Budget spent: 14 tool calls, 7 sources actually read (6 primary vendor pages + 1 third-party review), plus 3 search-result snippet sets used only as leads.

Note on source dates: KiotViet's `huong-dan-su-dung-kiotviet/*` help pages carry **no visible publication or last-updated date**. They are the vendor's own live product documentation, so they describe the shipping product as of the access date, but I cannot bound their age. Confidence ratings below reflect that.

## Findings

### A. Feature teardown

- {claim: "Stocktaking lives at Quản lý > Hàng hóa > Kiểm kho; a sheet is created with the `+ Kiểm kho` button. Items are added three ways: (1) search box / F3 product lookup, (2) pick a whole nhóm hàng hóa (category), (3) Excel import.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "The counting grid shows, per line: **Tồn kho** (system quantity), **Thực tế** (counted quantity, the input), **Chênh lệch** (variance) and **Giá trị lệch** (variance value = số lượng lệch × giá vốn). So counting is NOT blind — the system quantity sits next to the input field, and there is no documented blind-count toggle. Variance IS valued in money at cost price, not quantity only.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "The sheet has filter tabs: **Tất cả / Khớp (matched) / Lệch (variance) / Chưa kiểm (not yet counted)**. The existence of a 'Chưa kiểm' bucket means in-scope-but-uncounted lines are tracked as a distinct state during counting.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "Document statuses are only two: **Phiếu tạm** (draft, saved via `Lưu tạm`, editable via `Cập nhật`) and **Đã cân bằng kho** (balanced/finalized, via `Hoàn thành`). There is no documented third 'pending approval' status.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "On `Hoàn thành` the system auto-adjusts stock in one step, with no separate adjustment document: «hệ thống sẽ tự động cân bằng kho, cập nhật lại số lượng tồn kho về đúng bằng số lượng thực tế». Counting and stock adjustment are therefore the same action — no separation of duties between counter and approver is documented.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-hang-hoa/kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "A finalized sheet cannot be edited, but it can be **Hủy bỏ** (cancelled), which reverses the balancing and restores the prior stock levels. Draft sheets are editable.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-hang-hoa/kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "Counting per **lô / hạn sử dụng** is supported when the setting Thiết lập > Hàng hóa > «Quản lý tồn kho theo Lô, hạn sử dụng» is on: «Khi tạo phiếu kiểm kho, bạn cần chọn từng lô và nhập số lượng thực tế của lô đó». Lot tracking also covers nhập hàng, trả hàng, chuyển hàng, xuất hủy, bán hàng, with FEFO auto-suggestion on sale.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/hang-hoa-lo-han-su-dung/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: high, class: feature}

- {claim: "Scanning ergonomics: the add-item box has two modes toggled with F6 — normal mode (cursor jumps to the quantity field after selecting an item) and a quick/scan mode where each scan or Enter increments the counted quantity by 1. Keyboard shortcut F3 opens product search.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "Excel import into a count sheet uses a downloadable template with columns **Mã hàng, Số lượng** and a Serial/IMEI column, uploaded via `Chọn file dữ liệu`. The docs I read describe no preview/validation/diff step before the imported rows land in the sheet.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "There is an audit trail of counting activity on the sheet — a **Kiểm gần đây** section logging quantity additions/edits.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-kiem-kho/tao-phieu-kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "The mobile app supports the kiểm kho document lifecycle: create a phiếu kiểm kho, update a draft, cancel, print and search sheets.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/retail-hang-hoa/kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: medium, class: feature}

- {claim: "The F&B (bar/cafe/nhà hàng) variant of the kiểm kho guide adds a sheet **merge** operation ('completing or merging count sheets') alongside the same Khớp/Lệch review, suggesting multiple draft sheets can be consolidated — the closest thing found to multi-user parallel counting.", source URL: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-bar-cafe-nha-hang/kiem-kho/, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: low, class: feature}

### B. Packaging / tier gating

- {claim: "Vendor's own published prices (retail vertical): **Gói hỗ trợ 270.000đ/tháng** (1 branch, max 3 user accounts, basic inventory, no multi-warehouse), **Gói chuyên nghiệp 330.000đ/tháng** (unlimited users, extra branch 270k, multi-warehouse 150k per extra kho, basic Shopee/TikTok Shop), **Gói cao cấp 490.000đ/tháng** (extra branch 375k, multi-warehouse 150k/kho, full marketplace integration, AI analytics, API). Lodging vertical: 220k / 490k / 990k. No effective date printed on the page.", source URL: https://www.kiotviet.vn/phi-dich-vu, publisher: KiotViet (Citigo), pub_date: undated (page live 2026-09-21), accessed: 2026-09-21, confidence: medium-high, class: pricing}

- {claim: "Kiểm kho is not called out as a paid/tier-gated module anywhere on the price page; it sits under the general Hàng hóa/quản lý kho capability present from the base Gói hỗ trợ. What IS metered is **extra warehouses (kho phụ) at 150k/month each** and extra branches. Inference, not an explicit vendor statement.", source URL: https://www.kiotviet.vn/phi-dich-vu, publisher: KiotViet (Citigo), pub_date: undated, accessed: 2026-09-21, confidence: low, class: pricing}

- {claim: "Contradiction to chase: an aggregator lists 250k/310k/490k effective 01/05/2025 and a separate vendor announcement page exists at kiotviet.vn/kiotviet-thong-bao-dieu-chinh-gia-ban-san-pham-... — i.e. prices were adjusted upward to the 270/330/490 now shown. Aggregator figures are stale; vendor page wins.", source URL: https://nplgcorp.com/gia-phan-mem-kiotviet-bao-nhieu/ (seen as search snippet only, not fetched), publisher: NPLG Corp, pub_date: claims 2026, accessed: 2026-09-21, confidence: low, class: pricing}

### C. Customer voice

- {claim: "Third-party editorial review (Aug 2, 2026) lists praise for ease of use for non-technical merchants and broad inventory management, and criticisms of limited advanced automation, internet dependency and cost escalation when upgrading. Crucially it contains **no quoted users and no reports of stock-accuracy or kiểm kho problems** — it is editorial analysis, not user voice.", source URL: https://topdanhgia.vn/kiotviet-co-thuc-su-tot-khong/, publisher: topdanhgia.vn, pub_date: 2026-08-02, accessed: 2026-09-21, confidence: low (unsourced editorial, possibly affiliate), class: sentiment}

- {claim: "Competitor-published review (POS365, a direct rival) alleges KiotViet weaknesses including difficulty controlling staff fraud, weak mobile UI, slow support, no separate online vs offline sales reporting, and weak inventory forecasting/advanced analytics. Treat as adversarial marketing, not evidence.", source URL: https://www.pos365.vn/review-phan-mem-kiotviet-tinh-nang-uu-nhuoc-diem-bang-gia-8613.html (search snippet only, not fetched), publisher: POS365, pub_date: unknown, accessed: 2026-09-21, confidence: low, class: sentiment}

## Leads

- **Vendor price-change announcement page** `https://www.kiotviet.vn/kiotviet-thong-bao-dieu-chinh-gia-ban-san-pham-phan-mem-quan-ly-ban-hang/` — will carry a dated effective-date for the 270/330/490 tiers. Fetch next round to satisfy the ≤3-month pricing bar.
- **Vertical-specific kiểm kho guides exist and differ**: `retail-hang-hoa/kiem-kho`, `salon-hang-hoa/kiem-kho`, `huong-dan-bar-cafe-nha-hang/kiem-kho`, `huong-dan-hang-hoa/kiem-kho`, `ung-dung-tren-mobile-mobile-app/kiem-kho` (this last 404'd on the www host — try the `hotro.kiotviet.vn` host or the biz-vn.com mirror seen in search results). The F&B one mentions merging sheets; the retail one does not. Worth diffing them — the F&B version is where nguyên liệu/định lượng counting would surface.
- `hotro.kiotviet.vn` returned **HTTP 503** on the one URL I guessed; retry next round, it is likely the real help-center host with searchable articles and release notes.
- **No changelog/release-notes surface found** for KiotViet this run. The nearest signal is feature-launch marketing posts (e.g. the Lô & Hạn sử dụng launch announcement at `kiotviet.vn/phan-mem-quan-ly-kiotviet-ra-mat-tinh-nang-quan-ly-hang-hoa-theo-lo-va-han-su-dung/`). Chase that page for a date, and look for a `/tin-tuc/` or `/cap-nhat/` index.
- Real user voice was not reachable through a US-indexed search tool. Next round should target Facebook groups, YouTube comment threads (e.g. the "Cách kiểm kho trên điện thoại" video), and Vietnamese forums directly rather than via generic search.
- **Wedge hypothesis (unverified):** counting and stock adjustment being a single `Hoàn thành` action, with no approval status and no blind-count option, is the clearest structural gap versus an audit-grade design.

## Looked for but could not find

- **Snapshot / cut-off behaviour — NOT ESTABLISHED.** This is the highest-priority question and I could not answer it. None of the five kiểm kho help pages I read states whether the `Tồn kho` column on an open `Phiếu tạm` is frozen at sheet creation or re-read live at `Hoàn thành`, and none contains any warning to stop selling during a count. No mention of any freeze/lock/snapshot concept anywhere. My working hypothesis — explicitly **unverified belief, do not report as fact** — is that KiotViet re-evaluates current stock at finalization and simply sets tồn = thực tế, which would silently swallow any sale made mid-count. This needs to be settled by a trial account or by the hotro help center.
- **Unfinished / uncounted items at finalization — NOT ESTABLISHED.** A `Chưa kiểm` tab exists, so the system knows which lines were never counted, but no page I read says whether finalizing treats them as zero, leaves them unchanged, or blocks completion. One paraphrase suggested uncounted lines simply carry through to finalized status, but the underlying page does not state the stock effect, so I am not reporting it as a finding.
- **Approval step / permission separation** — no `phân quyền` documentation for kiểm kho found on any of the five guides. Absence in docs is suggestive but not proof; KiotViet does have a general role/permission system that likely has a Kiểm kho node.
- **Excel import preview/validation step** — not described. The docs jump from choosing the file to the populated sheet. Cannot say whether an error/mapping preview exists.
- **Unit conversion (thùng/lốc/cái) during counting** — no mention at all in any kiểm kho guide. KiotViet has đơn vị quy đổi as a product feature; whether the count sheet lets you count in a secondary unit is undocumented in what I read.
- **Multi-user parallel counting on one sheet** — nothing explicit. Only the F&B page's sheet-merge mention gestures at it.
- **Cycle / partial counting by area or zone** — partial counting *by category* is possible (add items by nhóm hàng hóa), but there is no concept of a location/area/aisle scope in the documentation.
- **Release notes / changelog** — no changelog surface located for KiotViet.
- **Genuine 1–3★ user reviews or forum threads about kiểm kho** — none retrieved. Every sentiment-flavoured result was either the vendor, a direct competitor, or an undated/affiliate review blog. Sentiment section above is thin and should be treated as near-empty.
