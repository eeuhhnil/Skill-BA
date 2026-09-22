# Digest: Sapo POS shift management / cash-drawer reconciliation

## Q1 — Capability: does Sapo POS have shift management, and what does it support?

- claim: Sapo POS has a "Quản lý ca bán hàng" (shift management) feature that must be enabled via a configuration toggle ("Quản lý ca" and "Quản lý két tiền" / cash-drawer management) in Cấu hình bán hàng before use.
  source: https://help.sapo.vn/quan-ly-ca-ban-hang
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: Opening a shift ("Mở ca") is done by pressing "Mở ca" on the POS sales screen and entering an optional opening cash advance ("Số tiền tạm ứng đầu ca"), then confirming.
  source: https://help.sapo.vn/quan-ly-ca-ban-hang
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: Closing a shift ("Đóng ca") requires entering the physically counted cash amount ("Số tiền mặt đếm được" — only shown when cash-drawer management is enabled) plus an optional note; the system compares counted vs. system-calculated amount (basic discrepancy detection implied).
  source: https://help.sapo.vn/quan-ly-ca-ban-hang
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: Shift screen has two panels — shift list at the branch, and a detail panel per shift showing "Tiền trong ca" (cash by payment method), "Đơn hàng" (orders/returns in the shift), and "Hoạt động" (activity log: open, close, cash withdrawal, cash deposit) — a manager audit view.
  source: https://help.sapo.vn/quan-ly-ca-ban-hang
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: A separate "Tạo và quản lý phiếu thu trên màn bán hàng POS" (POS receipt/cash voucher) feature and a general "Sổ quỹ" (cash book) exist, but it could not be confirmed whether these attach to/document shift-cash discrepancies specifically (fetch returned only nav/index content).
  source: https://help.sapo.vn/quan-ly-phieu-thu-pos
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: low
  class: capability-claim

- claim: Sapo Accounting (a related but distinct product from the POS shift screen) has a dedicated "Xử lý chênh lệch" (discrepancy handling) function for cash-count discrepancies during physical cash inventory — evidence of variance-handling capability in the Sapo ecosystem, but documented under Accounting's cash-inventory workflow, not confirmed as part of the POS "Kết ca" screen itself.
  source: https://help.sapo.vn/xu-ly-chenh-lech-khi-kiem-ke-tien-mat-tren-sapo-accounting
  publisher: Sapo (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: medium
  class: capability-claim

- claim: A third-party summary describes Sapo's shift tool as letting owners/managers "open/close shifts quickly, track transactions per shift, manage cash accurately, and generate clear shift reports" — consistent with but more marketing-worded than primary docs.
  source: search snippet aggregation citing help.sapo.vn
  publisher: Sapo (help.sapo.vn, via search snippet)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: medium
  class: capability-claim

**NOT CONFIRMED despite specific searching:**
- Explicit structured discrepancy/variance REASON field on the shift-close screen (only a generic free-text "Ghi chú" note was confirmed).
- Whether receipts/vouchers ("phiếu thu") can be attached as evidence for a shift discrepancy.
- Whether shift closing produces a dedicated printable report/receipt at time of close.
- Explicit filter controls on the shift list (by time/status/employee) — only the two-panel list+detail structure was confirmed; full article body was not fully retrievable (likely JS-rendered page).

## Q2 — Customer sentiment on shift-closing / cash reconciliation specifically

- claim: No customer reviews, forum posts, or community discussion specifically discussing Sapo's "kết ca"/cash-reconciliation feature (praise or complaint) were found. Searches for "Sapo kết ca lệch tiền" returned unrelated results (Sapo's own blog, a brand-impersonation warning, an unrelated GitHub issue, general license-resale complaints).
  source: search conducted 2026-09-22, no qualifying source found
  publisher: n/a
  pub_date: n/a
  accessed: 2026-09-22
  confidence: n/a
  class: other

- claim: General (non-shift-specific) third-party reviews of Sapo POS mention: new employees need 2-3 days to adjust due to many features/settings; iOS app reportedly lags with many orders; reporting cannot export raw data to Excel/Sheets and lacks custom report builder; mixed opinions on support responsiveness at peak hours. None named the shift-closing/cash-reconciliation feature specifically.
  source: search snippet aggregation (accgroup.vn, tino.vn, chukinhdoanh.com, kiotviet.net review page)
  publisher: multiple secondary/marketing-adjacent Vietnamese tech blogs; one source (kiotviet.net) is a direct competitor reviewing Sapo — low-trust for balanced sentiment
  pub_date: unknown
  accessed: 2026-09-22
  confidence: low
  class: customer-sentiment

- claim: Attempted to check Google Play reviews for "Sapo - Thu ngân" app for shift/cash mentions; fetch returned no usable review content (dynamically loaded).
  source: https://play.google.com/store/apps/details?id=com.sapo.fnb&hl=en_US
  publisher: Google Play (attempted, unsuccessful)
  pub_date: n/a
  accessed: 2026-09-22
  confidence: n/a
  class: other

## Leads
- Full body of https://help.sapo.vn/quan-ly-ca-ban-hang likely JS-rendered — a browser-capable fetch would likely surface more procedural detail (filters, discrepancy reason fields, print format).
- https://help.sapo.vn/xu-ly-chenh-lech-khi-kiem-ke-tien-mat-tren-sapo-accounting — worth checking whether this discrepancy mechanism surfaces inside the POS "Kết ca" flow or is a separate downstream accounting step.
- https://help.sapo.vn/quan-ly-phieu-thu-pos — worth a direct full read.
- Facebook groups for Vietnamese retail/shop owners not reachable via generic web search this session — likely richer source of unfiltered sentiment.
- App Store/Google Play review text itself needs a different retrieval method.

## Could not find
- Structured discrepancy/variance reason field (beyond generic note) on shift-close screen.
- Receipt/voucher attachment specifically for cash discrepancies.
- Printable shift-closing report/receipt format or content.
- Shift-list filter controls (by time/status/employee) beyond general list+detail layout.
- Any customer reviews/forum/community commentary specifically about the shift-closing/cash-reconciliation feature — only generic, non-feature-specific complaints, one from a competitor's own site.

Pricing/plans/tiers excluded throughout per scope.
