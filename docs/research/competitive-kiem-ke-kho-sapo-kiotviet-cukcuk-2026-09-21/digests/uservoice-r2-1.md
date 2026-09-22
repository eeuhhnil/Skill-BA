# User voice R2 — stocktaking / inventory in KiotViet, Sapo, CukCuk

Accessed: 2026-09-21. Method: bypassed web search (SEO sludge, as briefed) and went to
primary review stores. Google Play detail pages truncated before the review block on every
fetch and were abandoned. Apple's public customer-review RSS feeds
(`itunes.apple.com/vn/rss/customerreviews/...`) returned raw review text with star rating,
app version and date — these are the backbone of this digest. voz.vn returned HTTP 403 to
all fetches (bot-blocked).

**Headline: genuine first-hand user voice specifically about *kiểm kê / stocktaking* was
not found for any of the three vendors.** What was found is adjacent and still useful:
inventory *accuracy* and *sync* complaints. See "Looked for but could not find" — it is
the most important section in this file.

---

## Findings

### KiotViet

App identity verified this run: iOS `KiotViet` trackId 1146695068, seller "KiotViet
Technology Corporation", **2.92★ / 1,403 ratings**, last release 2026-09-21
(itunes.apple.com search API, accessed 2026-09-21). Android `net.citigo.kiotviet.manager`,
Play listing shows **2.9★** (play.google.com search page, accessed 2026-09-21).

- **claim:** Users report the mobile app displays inventory on hand incorrectly. Three
  separate reviewers posted this on the same day against the same build.
  - "Appp trên điện thoại hiển thị tồn kho không chính xác" — Lê VănTèo, **1★**, v2.5.991
  - "app trên điện thoại hiển thị tồn kho không chính xác" (title); body: "phần mềm lỗi"
    — Cá mồi ba cô gái, **1★**, v2.5.991
  - "App trên điện thoại hiển thị tồn kho không chính xác" — Linhlan1238&, **1★**, v2.5.991
  - source URL: https://itunes.apple.com/vn/rss/customerreviews/page=1/id=1146695068/sortby=mostrecent/json
  - publisher: Apple App Store (VN storefront) | pub_date: 2026-08-25 (all three)
  - accessed: 2026-09-21 | class: sentiment | star_rating: 1★ ×3
  - **confidence: medium.** The signal is on-topic and recent, but the three reviews are
    near-identical wording on one day against one build. That is either a real regression in
    2.5.991 that many users hit at once, or a brigade/templated campaign. Do not quote the
    "three users" framing as independent corroboration without a second source.

- **claim:** Sync backlog leaves orders stuck and unreconciled, unfixed over a long period.
  "App lỗi đang chờ đồng bộ 1 đống đơn. Bị lâu rồi không ai fix."
  - Như cáiqq, **1★**, v2.5.961 | pub_date: 2026-08-11
  - source URL: as above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: high (single specific dated complaint) | class: sentiment | star_rating: 1★
  - Relevance to stocktaking is inferential, not stated: unsynced orders are the classic
    mechanism behind a count that disagrees with the system. The user did not say that.

- **claim:** Absence of demand-forecasting / reorder intelligence off inventory turnover is
  a named gap. "Bao năm rồi, không chịu đầu tư cải tiến. Thời AI rồi mà không có tính năng
  tự động hoá thông minh ví dụ: - Thông báo nên nhập hàng gì, giảm nhập hàng gì dựa vào
  vòng quay tồn kho."
  - HOALE-ALEX, **1★**, v2.6.031 | pub_date: 2026-09-16
  - source URL: as above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: high | class: sentiment | star_rating: 1★
  - This is an inventory *analytics* gap, not a stocktake gap.

- **claim:** Other recent 1–2★ complaints are not inventory-related (Grab menu sync order
  scrambling, topping sync, e-invoice disconnects, lag/crashes, no bulk-delete of draft
  invoices). Reviewers: dphgtn 1★ v2.5.711 2026-04-22; Lena_Trịnh 1★ v2.5.621 2026-03-17;
  GNCL,., 2★ v2.5.481 2025-12-11.
  - source URL: https://itunes.apple.com/vn/rss/customerreviews/page=2/id=1146695068/sortby=mostrecent/json
  - publisher: Apple App Store (VN) | accessed: 2026-09-21 | confidence: high
  - class: sentiment | Recorded as a negative finding: the KiotViet pain surface visible in
    reviews is F&B/integration/stability, not stocktaking.

### Sapo

App identity verified this run: iOS `Sapo - Sales Management` trackId 979090133,
**3.46★ / 1,510 ratings**, last release 2026-09-17. Android `com.dkt.pos` shows **2.7★**.
Sapo ships many separate apps (Order 2.89★/405, Restaurant Management 3.85★/145,
Chat OmniAI 3.33★/33, Sapo 365 4.86★/565 but last released 2022-11-02).

- **claim:** **No user review in the most-recent page of the Sapo feed is about inventory
  or stocktaking.** Of ~40+ entries read, the on-topic count was zero; complaints cluster on
  support quality, sync outages, UI regressions and combo pricing.
  - source URL: https://itunes.apple.com/vn/rss/customerreviews/page=1/id=979090133/sortby=mostrecent/json
  - publisher: Apple App Store (VN) | accessed: 2026-09-21 | confidence: high
  - class: sentiment (negative finding)

- **claim:** General instability and failure to sync, with slow support.
  "Khi mua gói thì rất nhanh, quá trình làm vướng mắc thì liên hệ xử lý rất chậm chạp và
  cứng nhắt. Phần mềm hay bị lỗi, gián đoạn không đồng bộ được."
  - Tá Hoàng Danh, **1★**, v8.0.1 | pub_date: 2026-08-29
  - source URL: as above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: high | class: sentiment | star_rating: 1★

- **claim:** A v8.0.x update removed at-a-glance daily sales from the home surface.
  "Ko còn hiển thị doanh số bán hàng trong ngày. Phải kích vào trong mới xem được. Thà đừng
  cập nhật để v sài còn đỡ hơn. Fix bớt lỗi dùm với."
  - Mi nhon12, **2★**, v8.0.1 | pub_date: 2026-08-29
  - source URL: as above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: high | class: sentiment | star_rating: 2★
  - Adjacent signal on data-entry correctness: combo/bundle products price wrongly when a
    component price changes — "tạo combo mà giá combo không tự điều chỉnh theo giá thành
    phần khi giá thành phần thay đổi" (Shopee_mất dạy, **1★**, v8.0.0, 2026-08-27). Combos
    are a known source of stock-deduction error, but the user complained about price only.

### CukCuk (MISA)

App identity verified this run: iOS `CUKCUK - SALE` trackId 1106895954, **3.23★ / 950
ratings**, last release 2026-09-21; `Manager - CUKCUK` trackId 1097820618, **4.07★ / 632
ratings**, last release 2026-07-22. Android `vn.com.misa.qlnh` shows **2.6★**. Note
`CUKCUK Lite` (4.4★) last shipped 2019 and `MISA Support` (2.20★/767) last shipped 2022 —
stale, do not use.

- **claim:** The manager app has a real, user-named inventory gap: no way to enter raw
  material stock on hand from the manager app. "Phần quản lý kho cũng không thấy chỗ nhập ng
  vật liệu tồn kho" (same review also: reporting only shows the last 2 days, weekly, monthly).
  - cybermin, **3★**, v72 | pub_date: 2020-05-31
  - source URL: https://itunes.apple.com/vn/rss/customerreviews/page=1/id=1097820618/sortby=mostrecent/json
  - publisher: Apple App Store (VN) | accessed: 2026-09-21
  - **confidence: low — this is ~6 years old and almost certainly superseded.** It is the
    single most on-topic piece of user voice found in this entire run, and it is stale.
    Flagging it as a hypothesis to re-verify, not as a current finding.

- **claim:** Purchase/goods-receipt could not be done on iOS manager, only on PC.
  "Hiện trên IOS không hỗ trợ về nhập mua hàng (app quản lý không có) chỉ làm được trên Pc."
  - quan68db, **5★** (praise-framed but lists gaps), v R77.1 | pub_date: 2020-11-19
  - source URL: as above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: low (stale, 2020) | class: sentiment | star_rating: 5★
  - Note the rating/content mismatch: 5★ attached to a list of missing features. Treat the
    star as noise.

- **claim:** Cross-device data desync is the dominant recent CukCuk complaint, with concrete
  operational damage. Examples:
  - "Phần mềm đơ lòi mắt, thông tin giữa các thiết bị ko đồng bộ nếu thay đổi gì phải cập
    nhật hết các máy" — hacobi1102, **1★**, vR138, 2025-11-14 (Manager feed)
  - "App lỗi thường xuyên, bán hàng xong qua ngày mới nhân viên không đồng bộ được dữ liệu
    phải xoá app đi tải lại nhiều lần" — Bao117HXH, **1★**, vR144.2, 2026-04-02 (SALE feed)
  - "Quán tôi dùng app này, đợt tết này các thiết bị iphone cứ không đồng bộ được số bàn
    trống trong quán, làm quán phục vụ chậm, ảnh hưởng bán hàng, chất lượng dịch vụ và doanh
    thu quán" — Lilipham1505, **2★**, vR142, 2026-02-21 (SALE feed, Tết period)
  - "App lỗi, lag, ko đồng bộ, phí là cao nhất" — Mrneo1989, **1★**, vR129.1, 2025-04-19
  - source URLs: https://itunes.apple.com/vn/rss/customerreviews/page=1/id=1106895954/sortby=mostrecent/json
    and the Manager feed above | publisher: Apple App Store (VN) | accessed: 2026-09-21
  - confidence: high | class: sentiment | star_rating: 1★, 1★, 2★, 1★
  - The Bao117HXH one is the closest thing found to "a day's transactions did not land" —
    the precondition for a count disagreeing with the system. He did not mention counting.

---

## Leads

- **Google Play review text is reachable, just not by naive WebFetch.** Every detail-page
  fetch truncated before the reviews. Package ids are now confirmed:
  `net.citigo.kiotviet.manager`, `com.dkt.pos` (+ `com.sapo.retail.pos`, `com.sapo.fnb*`),
  `vn.com.misa.qlnh`. A scripted `google-play-scraper`-style pull, or fetching the reviews
  XHR endpoint directly, would unlock the largest pool of Vietnamese user voice by far
  (KiotViet Android alone is far higher-volume than its 1,403 iOS ratings).
- **Apple RSS feeds paginate to page=10.** Only pages 1–2 (KiotViet) and page 1 (Sapo,
  CukCuk ×2) were read. Deeper pages, plus `sortby=mostcritical`, are cheap and likely to
  surface more inventory-specific text.
- **Untouched Apple feeds with plausible inventory voice:** Sapo Order (1481818437, 2.89★),
  Sapo Restaurant Management (1493257930), KiotViet Quản lý Nhà hàng (1421096863),
  KiotViet Salon (1593051989), KiotViet Hotel (1668949503).
- **voz.vn is 403 to WebFetch but the threads exist and are on-topic.** Confirmed live URLs
  worth retrieving another way: `voz.vn/t/quan-ly-hang-ton-kho.1072775/page-2`,
  `voz.vn/t/buon-ban-cua-hang-bi-mat-hang.963767/`,
  `voz.vn/t/tu-van-phan-mem-quan-ly-ban-hang.286845/page-2`,
  `voz.vn/t/phan-mem-quan-ly-ban-hang-offline.1065456/`. A cached/mirror route or a
  browser-capable tool should be round 3's first move.
- **forum.misa.vn is indexable and has a dedicated CukCuk board**
  (`forum.misa.vn/forums/misa-cukcuk-phan-mem-quan-ly-nha-hang.37/`). Searching it returned
  only MISA-authored release notes and template threads in this run — but the board itself
  was never paged through directly. Worth one direct crawl of the board index.
- **Adjacent competitor signal worth ignoring:** the tinhte "Review So Sánh Kiotviet Và
  DanTriSoft" thread is almost certainly DanTriSoft-authored. Not used here, per brief.

---

## Looked for but could not find

Blunt version:

1. **No first-hand user account of a stocktake going wrong was found for any of the three
   products.** Nothing about a count being overwritten, sales landing mid-count, a count
   having to be redone, stock being wrong *during* a count, or stock moving *after* a count
   was posted. That was the brief's highest-value target and it returned zero across
   ~9 sources. This is a real finding, not a search failure to paper over.

2. **The word "kiểm kê" / "kiểm kho" / "kiểm hàng" did not appear in a single genuine user
   review read this run.** Every hit on those terms in general web search was vendor help
   documentation or affiliate SEO, exactly as in round 1. Users who write app reviews are
   cashiers and owners complaining about crashes, sync, fees and support — not about the
   periodic stocktake workflow. Stocktaking appears to be a back-office/desktop task that
   simply does not generate mobile app-store reviews.

3. **Sapo has essentially no public user voice on inventory at all.** 40+ recent reviews
   read, zero on-topic. Do not manufacture a Sapo inventory narrative from this dataset.

4. **The only directly on-topic inventory-feature complaint found (CukCuk, no raw-material
   stock entry in the manager app) is from 2020** and should be assumed fixed unless
   re-verified.

5. **Google Play reviews — the biggest pool — were not actually read.** Every detail-page
   fetch truncated. All Play-derived numbers here (2.9★ KiotViet, 2.7★ Sapo, 2.6★ CukCuk)
   come from the Play *search* results page, not from reading reviews. Treat those star
   figures as indicative only; one search-page summary also returned implausible figures
   (e.g. "2.16 million reviews" for KiotViet, "100 million downloads" for CukCuk) which are
   extraction errors and are deliberately not carried into the findings above.

6. **voz.vn, tinhte.vn (usable threads), webketoan.vn: no content retrieved.** voz 403s;
   webketoan produced no result at all. YouTube comments and Facebook groups were not
   attempted — budget exhausted.

7. **Fake-review watch:** no burst of generic 5★ one-liners was observed in the feeds read.
   The one anomaly is the opposite — the identical-text 1★ KiotViet cluster on 2026-08-25,
   flagged inline above.
