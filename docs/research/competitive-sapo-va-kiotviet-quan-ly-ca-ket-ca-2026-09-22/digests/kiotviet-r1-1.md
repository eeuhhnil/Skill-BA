# Digest: KiotViet shift management / cash-drawer reconciliation (mở ca / kết ca)

## Q1: Does KiotViet have a shift management feature, and what does it support?

- claim: KiotViet's POS requires cashiers to open a shift ("Mở ca làm việc") before processing sales; the opening popup requires entering a starting cash amount plus an optional note.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/ket-ca-fnb/
  publisher: KiotViet (official help center, F&B module)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: The system tracks all transactions made under the logged-in cashier's open shift in real time; if internet connectivity drops mid-shift, transactions completed during the outage are not recorded in the shift log (a noted limitation).
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/ket-ca-fnb/
  publisher: KiotViet (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: At shift end, cashiers select "Đóng ca làm việc" (close shift) and enter the actual cash handed over plus an optional note; they can then print a "phiếu bàn giao" (handover/settlement voucher) if a receipt printer is configured.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/ket-ca-fnb/
  publisher: KiotViet (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: The shift-closing report shows total revenue, quantity of items sold, revenue broken down by item, and collection/payment (thu chi) amounts; cashiers can review order details and reconcile counted cash against system figures, and can print the settlement document.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-xem-bao-cao-ket-ca/
  publisher: KiotViet (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: high
  class: capability-claim

- claim: Managers can pull a consolidated summary of each employee's shift ("tổng hợp chi tiết từng ca làm việc của nhân viên") at any time, supporting audit of shift history; documentation frames the feature as helping monitor inventory levels per shift to catch discrepancies/fraud.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-xem-bao-cao-ket-ca/
  publisher: KiotViet (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: medium
  class: capability-claim

- claim: KiotViet help content states the shift-closing feature links all payment transactions to the cashier account that opened the shift "for easy reconciliation if discrepancies occur," and automatically summarizes revenue by payment method (cash, bank transfer, card) with a printable handover receipt; supported on both counter desktop app and mobile.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/hotel-ket-ca/ket-ca/ (search-snippet derived; not independently fetched)
  publisher: KiotViet (official help center, hotel module)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: medium
  class: capability-claim

- claim: Could NOT verify: (a) a structured discrepancy/variance "reason" field distinct from the general note field, (b) a photo/receipt/voucher attachment mechanism for discrepancies, (c) a manager-facing shift-history list with filters by time range/status/employee. Official pages fetched describe cash entry, review, and printing only.
  source: https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/ket-ca-fnb/ ; https://www.kiotviet.vn/huong-dan-su-dung-kiotviet/huong-dan-xem-bao-cao-ket-ca/
  publisher: KiotViet (official help center)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: medium
  class: capability-claim

## Q2: Customer sentiment on the shift-closing / cash reconciliation feature

- claim: A third-party retail-tech blog analyzing cashier fraud methods on KiotViet-type systems states that even with computerized tracking, employees can still defraud owners (voiding receipts after collecting cash, clock-tampering to hide a sale from shift reports, reducing a saved bill amount to skim the difference), calling such discrepancies "extremely difficult for owners to detect" — framed as a general control gap, not a KiotViet-specific design flaw; recommends cross-checks/audits/video alongside the software.
  source: https://www.kiotviet.net/2023/08/gian-lan-o-kiotviet-da-bill.html
  publisher: kiotviet.net (unofficial third-party blog, NOT the official kiotviet.vn site)
  pub_date: 2023-08
  accessed: 2026-09-22
  confidence: medium (single source, third-party, unverified authorship)
  class: customer-sentiment

- claim: A competing POS vendor's review site states KiotViet logs detailed employee action history (price edits, invoice cancellations) to help owners "detect anomalies immediately," but contains no direct praise/complaints about the shift-closing workflow itself.
  source: https://www.pos365.vn/review-phan-mem-kiotviet-tinh-nang-uu-nhuoc-diem-bang-gia-8613.html
  publisher: POS365 (competing POS vendor's review/blog)
  pub_date: unknown
  accessed: 2026-09-22
  confidence: low (competitor-authored, tangential)
  class: customer-sentiment

- claim: Search-aggregated (unconfirmed attribution) suggestion that KiotViet is commonly criticized for being "difficult to control employee fraud," weaker mobile interface, slower support, comparatively weak security — could not confirm the specific originating source(s).
  source: aggregated across pos365.vn, topdanhgia.vn, kiot-viet.com (exact attribution unconfirmed)
  publisher: multiple third-party Vietnamese review/comparison blogs
  pub_date: unknown
  accessed: 2026-09-22
  confidence: low
  class: customer-sentiment

## Leads
- Hotel-module shift-closing pages (kiotviet.vn/tinh-nang-ket-ca-tren-phan-mem-quan-ly-khach-san-kiotviet/, .../hotel-ket-ca/ket-ca/) — only skimmed via snippet, likely more detail on discrepancy handling/manager reporting.
- YouTube "Mở ca, kết ca thu ngân trên phần mềm KiotViet mới nhất | Mr Quản" (watch?v=Zf51-unQTjY) — UI walkthrough, not viewed.
- topdanhgia.vn "KiotViet có thực sự tốt không?" — not fetched.
- Targeted Facebook-group search (e.g. "kết ca lệch tiền", "kết ca báo lỗi") not yet tried — generic queries returned no on-topic community discussion this round.

## Could not find
- No official documentation confirming a dedicated variance-reason field separate from the general note field.
- No official documentation or user discussion confirming photo/receipt attachment for discrepancies.
- No official documentation describing a filterable (time/status/employee) shift-history list screen for managers — closest evidence is general "pull summary anytime" language.
- No genuine first-person customer reviews/forum/Facebook posts specifically on the kết ca/cash-reconciliation feature found within budget — largely unanswered, needs more targeted search.

Pricing/plans/tiers excluded throughout per scope.
