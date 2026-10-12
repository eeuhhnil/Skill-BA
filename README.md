# Hướng dẫn dùng Skill theo quy trình BA

> Dành cho BA và PO. Tài liệu này cho biết **ở mỗi bước của quy trình BA nên gọi skill nào, gọi thế nào, và nhận lại được gì**.
> Ví dụ xuyên suốt: nghiệp vụ **Kiểm kê kho**.
>
> 🛠️ **Lần đầu dùng?** Cài đặt theo [HUONG-DAN-CAI-DAT.md](HUONG-DAN-CAI-DAT.md) trước.

---

## 1. Bức tranh tổng thể

Quy trình BA của công ty có 6 bước. **Skill chỉ hỗ trợ 3 bước tạo tài liệu: 1, 3, 5.** Các bước 2, 4, 6 là họp và bàn giao, do người thực hiện.

```
 ┌─────────────────────┐   ┌─────────────────┐   ┌─────────────────────┐
 │ 1. GIẢI PHÁP SƠ BỘ  │──▶│ 2. CHỐT PHẠM VI │──▶│ 3. LUỒNG & FIGMA    │
 │    🤖 có skill      │   │    👥 họp       │   │    🤖 có skill      │
 └─────────────────────┘   └─────────────────┘   └─────────────────────┘
                                                            │
 ┌─────────────────────┐   ┌─────────────────┐   ┌──────────▼──────────┐
 │ 6. ĐÀO TẠO DỰ ÁN    │◀──│ 5. GIẢI PHÁP    │◀──│ 4. REVIEW & CHỐT    │
 │    👥 bàn giao      │   │    CHI TIẾT     │   │    👥 họp           │
 └─────────────────────┘   │    🤖 có skill  │   └─────────────────────┘
                           └─────────────────┘
```

Mỗi skill lấy **đầu ra của skill trước làm đầu vào**, nên chỉ cần đi đúng thứ tự là tài liệu tự nối với nhau:

```
 BƯỚC 1                                                            BƯỚC 3                         BƯỚC 5
 ──────────────────────────────────────────────────────────────    ────────────────────────────   ─────────
 brainstorming ─▶ deep-recon ─▶ product-brief ─▶ impact-analysis   ux ─▶ easypos-design           srs
      │               │              │                 │              │             │              │
      ▼               ▼              ▼                 ▼              ▼             ▼              ▼
 brainstorm-     research.md     brief.md          impact.md     wireframe      màn Figma       srs.md
 intent.md                                                        trắng đen      có màu
                                     └──────────────┬──────────────────┴─────────────┘              ▲
                                                    └───────────── srs tự đọc ──────────────────────┘
```

---

## 2. Cách gọi skill

Có 2 cách, cả hai đều được:

```
 Cách 1 — gõ tên skill:        /product-brief
 Cách 2 — nói tự nhiên:        "Viết giải pháp sơ bộ cho nghiệp vụ kiểm kê kho"
                               → Claude tự nhận ra và gọi skill phù hợp
```

**Mẹo:**
- **Mỗi skill nên chạy trong một cuộc trò chuyện mới.** Tài liệu đã lưu thành file nên skill sau vẫn đọc được. Cuộc trò chuyện ngắn thì Claude làm chính xác hơn.
- **Đưa đủ đầu vào ngay từ đầu:** yêu cầu khách hàng, biên bản họp, link Confluence, file của bước trước. Skill đọc trước rồi chỉ hỏi những gì còn thiếu.
- **Đang làm dở có thể dừng.** Mỗi skill ghi nhật ký (`.memlog.md`), lần sau gọi lại, skill sẽ hỏi bạn có muốn làm tiếp không.

---

## 3. BƯỚC 1: Giải pháp sơ bộ

**Mục tiêu:** làm rõ yêu cầu, nghiên cứu đối thủ, đề xuất hướng giải quyết.
**Đầu ra chính:** `brief.md` theo mẫu Giải pháp sơ bộ của công ty, kèm đánh giá ảnh hưởng.

```
  Yêu cầu từ KH / Sales
          │
          ▼
  ┌───────────────────┐   Cần nhiều hướng giải pháp?
  │ 1.1 BRAINSTORMING │   Không cần thì bỏ qua
  └─────────┬─────────┘
            ▼
  ┌───────────────────┐   Cần xem đối thủ làm thế nào?
  │ 1.2 DEEP-RECON    │   Không cần thì bỏ qua
  └─────────┬─────────┘
            ▼
  ┌───────────────────┐
  │ 1.3 PRODUCT-BRIEF │   ◀── BẮT BUỘC
  └─────────┬─────────┘
            ▼
  ┌───────────────────┐
  │ 1.4 IMPACT        │   ◀── BẮT BUỘC
  └─────────┬─────────┘
            │
      Phát hiện ảnh hưởng lớn? ──── Có ───▶ quay lại 1.3 sửa brief
            │ Không
            ▼
     Sang Bước 2 (họp chốt phạm vi)
```

### 1.1 Brainstorming (không bắt buộc): `brainstorming`

| | |
|---|---|
| **Khi nào dùng** | Yêu cầu còn mơ hồ, hoặc cần nhiều hướng giải pháp trước khi chọn |
| **Câu gọi mẫu** | `Brainstorm giúp tôi hướng giải quyết cho nghiệp vụ kiểm kê kho. Mục tiêu: giảm thời gian kiểm kê cho cửa hàng có trên 1000 mã hàng` |
| **Đầu vào** | Yêu cầu của khách hàng (file hoặc dán vào chat) |
| **Đầu ra** | `docs/<nghiệp-vụ>/brainstorming/brainstorm-intent.md` |

**Skill sẽ làm gì:**

```
 ① Hỏi chủ đề + mục tiêu
 ② Mở trang chọn chế độ và kỹ thuật (mô tả tiếng Việt)
    → tick chọn → bấm "Copy prompt" → dán lại vào chat
 ③ Chạy từng kỹ thuật, mỗi lần một câu hỏi
 ④ Khi đủ ý: thu hẹp và chọn (nên dùng MoSCoW: Must/Should/Could/Won't)
 ⑤ Xuất brainstorm-intent.md
```

**Chọn chế độ nào:**

| Chế độ | Ai nghĩ ý tưởng | Nên dùng khi |
|---|---|---|
| **Facilitator** | Chỉ BA; Claude đặt câu hỏi | BA đã hiểu nghiệp vụ, cần được "khai thác" |
| **Creative Partner** ⭐ | BA là chính, Claude góp thêm | **Dùng mặc định** |
| **Ideate for me** | Claude tự làm hết | Cần nhanh, chỉ muốn xem gợi ý |

**Kỹ thuật nên chọn cho BA:** How Might We · Job to Be Done · Assumption Reversal · Failure Analysis · Five Whys

### 1.2 Nghiên cứu đối thủ (không bắt buộc): `deep-recon`

| | |
|---|---|
| **Khi nào dùng** | Cần biết đối thủ đã làm tính năng này thế nào, hoặc người dùng phàn nàn gì |
| **Câu gọi mẫu** | `Nghiên cứu đối thủ Sapo, KiotViet, CukCuk về tính năng kiểm kê kho, để quyết định EasyPOS nên làm những gì` |
| **Đầu vào** | Tên đối thủ + **quyết định cần đưa ra** (bắt buộc) |
| **Đầu ra** | `docs/<nghiệp-vụ>/research/competitive-<chủ-đề>/research.md` |

> ⚠️ Skill đã được cấu hình **không nghiên cứu giá và các gói phần mềm**, chỉ tập trung vào tính năng, định vị và phản hồi của người dùng.

**Skill cho chọn 1 trong 3 cách:**

```
 ┌────────────────────────────────────────────────────────────────────┐
 │ RUN      Claude tự tìm trên web ngay tại đây                       │
 │          → Nhanh, trọn gói, tốn token hơn                          │
 ├────────────────────────────────────────────────────────────────────┤
 │ DRAFT    Claude soạn prompt → BA dán vào ChatGPT/Gemini/Perplexity │
 │   +      → tải báo cáo về → gọi lại skill: "process báo cáo này"   │
 │ PROCESS  → Rẻ hơn, phải qua tay 1 lần                              │
 └────────────────────────────────────────────────────────────────────┘
```

**Loại nghiên cứu hay dùng:**
- `competitive`: mổ xẻ đối thủ cụ thể.
- `user-voice`: người dùng khen chê gì (review, group, forum).

**Cách đọc kết quả:** mỗi thông tin có nguồn `[n]` và nhãn độ tin cậy. Thông tin gắn **unverified** (chưa kiểm chứng) hoặc **disputed** (các nguồn mâu thuẫn) thì cần xem lại trước khi đưa vào brief.

### 1.3 Viết Giải pháp sơ bộ (bắt buộc): `product-brief`

| | |
|---|---|
| **Câu gọi mẫu** | `Viết giải pháp sơ bộ cho nghiệp vụ kiểm kê kho. Đầu vào: docs/kiem-ke-kho/brainstorming/brainstorm-intent.md và docs/kiem-ke-kho/research/.../research.md` |
| **Đầu vào** | Yêu cầu KH + `brainstorm-intent.md` + `research.md` (có file nào đưa file đó) |
| **Đầu ra** | `docs/<nghiệp-vụ>/brief/brief.md` (+ `addendum.md`) |

**Skill cho chọn 1 trong 2 cách:**

```
 FAST PATH                              COACHING PATH
 ─────────────────────────────          ─────────────────────────────
 Hỏi gộp 1–2 câu                        Đi từng phần cùng BA
 → Viết luôn cả brief                   → Phản biện chỗ còn mỏng
 → Chỗ tự đoán gắn [ASSUMPTION]         → Viết lần lượt từng mục
 Hợp khi: cần gấp                       Hợp khi: nghiệp vụ phức tạp
```

**Brief có 5 phần** (mẫu của công ty):

```
 1. Làm rõ yêu cầu      ← khách hàng, câu chuyện, hiện trạng, điểm đau
 2. Yêu cầu nghiệp vụ   ← các nhóm việc + mục tiêu đo được
 3. Giải pháp nghiệp vụ ← UI (1–2 dòng), logic, quy trình, phạm vi ảnh hưởng
 4. Câu hỏi mở          ← 👥 mang vào buổi họp Bước 2
 5. Ghi chú cho Bước 5  ← chi tiết nhỏ (thêm cột, điều kiện) để dành viết SRS
```

**Quy ước:**
- Brief dài **1–2 trang**. Phần chi tiết hơn được đưa sang `addendum.md`.
- Tìm và sửa hết các nhãn `[ASSUMPTION]` trước khi họp.

**Chế độ khác của skill:**
- `Cập nhật brief kiểm kê kho: <thay đổi>`: sửa brief sau buổi họp chốt ở Bước 2.
- `Kiểm tra brief kiểm kê kho`: skill phản biện, chỉ rõ từng dòng chưa ổn.

### 1.4 Đánh giá ảnh hưởng (bắt buộc): `impact-analysis`

| | |
|---|---|
| **Câu gọi mẫu** | `Đánh giá ảnh hưởng của docs/kiem-ke-kho/brief/brief.md` |
| **Đầu vào** | `brief.md` |
| **Đầu ra** | `docs/<nghiệp-vụ>/impact/impact.md` |

**Skill sẽ làm gì:**

```
 ① Tóm tắt thay đổi: đọc dữ liệu gì, ghi ra dữ liệu gì
 ② Quét Confluence space của nhóm (chỉ đọc, không sửa trang nào)
 ③ Tìm các chức năng/màn hình/dữ liệu bị ảnh hưởng
 ④ Lập ma trận tác động + sơ đồ phụ thuộc
 ⑤ Chỉ ra MÂU THUẪN: giữa brief và Confluence, và giữa các trang Confluence với nhau
```

> 💡 Nếu `impact.md` có **tác động mức cao** hoặc **mâu thuẫn**, quay lại 1.3 để cập nhật brief **trước** khi họp chốt. Làm vậy thì không phải vẽ lại wireframe ở Bước 3.

### ✅ Checklist hoàn thành Bước 1

- [ ] `brief.md` không còn nhãn `[ASSUMPTION]`
- [ ] Mục 4 "Câu hỏi mở" đã liệt kê đủ để mang vào họp
- [ ] `impact.md` không còn mâu thuẫn chưa xử lý
- [ ] Đã đẩy brief + impact lên Confluence (nếu cần PO/PM đọc trước buổi họp)

---

## 4. BƯỚC 3: Xây dựng Luồng & Figma

**Mục tiêu:** chốt luồng và bố cục trước, rồi mới lên màu.
**Nguyên tắc:** vẽ trắng đen trước (nhanh, sửa dễ), chốt xong mới lên Figma màu (tốn công hơn).

```
  brief.md (đã chốt ở Bước 2)
          │
          ▼
  ┌────────────────────────────┐
  │ 3a. WIREFRAME TRẮNG ĐEN    │   ux
  │     luồng + bố cục màn     │   → file .excalidraw
  └─────────────┬──────────────┘
                │
        Team duyệt luồng? ──── Chưa ───▶ sửa wireframe
                │ Rồi
                ▼
  ┌────────────────────────────┐
  │ 3b. MÀN FIGMA CÓ MÀU       │   easypos-design
  │     đúng design system     │   → frame trên Figma
  └─────────────┬──────────────┘
                ▼
     Sang Bước 4 (họp review & chốt)
```

### 3a. Wireframe trắng đen: `ux`

| | |
|---|---|
| **Câu gọi mẫu** | `/ux Vẽ luồng và wireframe trắng đen cho nghiệp vụ kiểm kê kho từ docs/kiem-ke-kho/brief/brief.md. Chỉ cần luồng và bố cục, chưa cần màu sắc` |
| **Đầu vào** | `brief.md` (+ `impact.md`) |
| **Lưu ý** | Nên gõ `/ux` ở đầu câu. Skill này chưa nhận câu nói tự nhiên bằng tiếng Việt |
| **Đầu ra** | `docs/<nghiệp-vụ>/ux/EXPERIENCE.md` (luồng, trạng thái, hành vi) và `wireframes/*.excalidraw` |

**Wireframe cần trả lời được 4 câu hỏi:**

```
 ┌─────────────────────────────┐
 │ ←  Phiếu kiểm kê            │   ① Màn có ĐỦ thông tin chưa?
 ├─────────────────────────────┤
 │ Kho: [__________ ▼]         │   ② Thứ tự các khối, vị trí nút?
 │ Tìm hàng: [_____________]   │
 │ ┌─────┬──────┬──────┬─────┐ │   ③ Lỗi hiện ở đâu, nội dung
 │ │ Mã  │ Tồn  │ Thực │ Lệch│ │      câu thông báo là gì?
 │ ├─────┼──────┼──────┼─────┤ │
 │ │ ... │ ...  │ ...  │ ... │ │   ④ Bấm vào thì đi đâu,
 │ └─────┴──────┴──────┴─────┘ │      có thiếu màn nào không?
 │ ⚠ Lỗi hiển thị ở đây        │
 │   [Lưu tạm]  [Hoàn thành]   │
 └─────────────────────────────┘
```

> 💡 Mở file `.excalidraw` bằng excalidraw.com hoặc extension Excalidraw trong VS Code để xem và chỉnh tay.
> ⚠️ Ở bước này **chỉ lấy `EXPERIENCE.md` và wireframe**. Nếu skill đề nghị làm bảng màu, hướng thiết kế hay bản mock HTML thì **từ chối**, vì phần hình thức do `easypos-design` lo ở 3b.

### 3b. Màn Figma có màu: `easypos-design`

| | |
|---|---|
| **Câu gọi mẫu** | `Chuyển wireframe docs/kiem-ke-kho/ux/wireframes/phieu-kiem-ke.excalidraw sang Figma: <link file Figma>` |
| **Đầu vào** | File `.excalidraw` **đã chốt** + link Figma |
| **Đầu ra** | Frame màu trên Figma + `docs/<nghiệp-vụ>/ux/figma/figma-log.md` |

**Skill sẽ làm gì:**
- **Giữ đúng bố cục và nội dung của wireframe.** Skill không tự thêm hay bớt trường, nút hoặc bước.
- **Chỉ dùng component và màu từ library EasyPOS**, không tự vẽ tay.
- **Thành phần library chưa có** thì skill làm bản nháp, để ở page `Chờ duyệt` và báo lại cho designer.
- **Ghi lại mọi thứ trong `figma-log.md`:** link từng màn, các giả định `[ASSUMPTION]`, câu hỏi mở.

**Các chế độ khác của skill:**
- `Kiểm tra màn Figma <link> theo design system`: chấm xem màn đã đúng chuẩn EasyPOS chưa.
- `Cập nhật màn <tên> theo wireframe mới`: skill tạo phiên bản mới cạnh bản cũ, không sửa đè.

### ✅ Checklist hoàn thành Bước 3

- [ ] Luồng trong `EXPERIENCE.md` đã có đủ nhánh lỗi và trường hợp biên
- [ ] Wireframe trắng đen đã được team đồng ý **trước khi** lên Figma
- [ ] `figma-log.md` không còn `[ASSUMPTION]` hoặc câu hỏi mở chưa trả lời
- [ ] Thành phần ở page `Chờ duyệt` đã báo cho designer

---

## 5. BƯỚC 5: Viết Giải pháp chi tiết (SRS)

**Mục tiêu:** đặc tả rule, business rule, edge case để dev và QC làm theo.
**Đầu ra:** `srs.md` theo mẫu SRS của công ty.

```
   brief.md ──────┐
   impact.md ─────┼──▶ ┌──────────────┐     ┌───────────────┐
   wireframes ────┘    │  srs CREATE  │ ──▶ │ srs VALIDATE  │ ──▶ Bước 6
   (tự tìm)            └──────────────┘     └───────┬───────┘
                                                    │ còn lỗi
                                                    ▼
                                             sửa rồi kiểm tra lại
```

### `srs`

| | |
|---|---|
| **Câu gọi mẫu** | `Viết SRS cho nghiệp vụ kiểm kê kho` |
| **Đầu vào** | Skill **tự tìm** `brief.md`, `impact.md`, file `.excalidraw` và `figma-log.md` trong `docs/<nghiệp-vụ>/` |
| **Đầu ra** | `docs/<nghiệp-vụ>/srs/srs.md` |

**Skill sẽ làm gì:**

```
 ① KIỂM TRA CONFLUENCE TRƯỚC: nghiệp vụ này đã có SRS chưa?
    ├─ Có rồi   → đề nghị chuyển sang UPDATE (không tạo bản thứ hai)
    └─ Chưa có  → tiếp tục
 ② Đọc brief + impact + wireframe
 ③ Viết SRS theo mẫu công ty:
      Lịch sử thay đổi
      → Nguồn gốc thay đổi
      → Nội dung thay đổi (As-Is/To-Be, user story, CSDL, danh sách chức năng)
      → Chi tiết chức năng (màn hình, luồng sự kiện, lỗi, business rule)
      → Luồng ảnh hưởng
 ④ Chỗ tự suy luận gắn [ASSUMPTION]
```

**Các chế độ khác:**
- `Cập nhật SRS kiểm kê kho: <thay đổi>`. Nguồn có thể là file hoặc trang Confluence, skill tự tải trang về trước khi sửa.
- `Kiểm tra SRS kiểm kê kho`: tự kiểm tra trước khi bàn giao ở Bước 6.

> 💡 Sơ đồ luồng trong SRS được viết bằng `mermaid`.

### ✅ Checklist hoàn thành Bước 5

- [ ] Đã chạy `srs` ở chế độ Validate và sửa hết các lỗi
- [ ] Không còn `[ASSUMPTION]`
- [ ] Mỗi màn trong SRS khớp với màn Figma đã chốt ở Bước 4
- [ ] Đã gửi SRS cho dev/QC trước buổi đào tạo

---

## 6. Confluence (chỉ đọc)

Skill **không đẩy tài liệu lên Confluence**. Mọi tài liệu chỉ lưu dạng file Markdown trong `docs/`.

Skill chỉ **đọc** Confluence (space của nhóm, khai báo ở Bước 6.3 của `HUONG-DAN-CAI-DAT.md`) khi cần:
- `impact-analysis` quét các trang có sẵn để tìm chức năng, dữ liệu bị ảnh hưởng.
- `srs` kiểm tra nghiệp vụ đã có SRS trên Confluence chưa, hoặc tải một trang có sẵn về để cập nhật.

Để đọc được, cần có Personal Access Token của Confluence, đặt vào biến môi trường `CONFLUENCE_PAT` hoặc file `~/.confluence-pat`. **Không bao giờ dán token vào chat.**

---

## 7. Sơ đồ thư mục tài liệu

Mỗi nghiệp vụ có **một thư mục riêng** trong `docs/`, đặt theo tên nghiệp vụ không dấu (vd `kiem-ke-kho`). Mọi tài liệu của nghiệp vụ đó nằm chung bên trong, mỗi skill một thư mục con:

```
 docs/
 └── kiem-ke-kho/                          ← tên nghiệp vụ
     ├── brainstorming/
     │   └── brainstorm-intent.md          ← 1.1
     ├── research/competitive-<chủ-đề>/
     │   └── research.md                   ← 1.2
     ├── brief/
     │   ├── brief.md                      ← 1.3  ⭐
     │   └── addendum.md
     ├── impact/
     │   └── impact.md                     ← 1.4  ⭐
     ├── ux/
     │   ├── EXPERIENCE.md                 ← 3a
     │   ├── wireframes/*.excalidraw       ← 3a  ⭐
     │   └── figma/figma-log.md            ← 3b
     └── srs/
         └── srs.md                        ← 5   ⭐
```

Lần đầu làm một nghiệp vụ, skill sẽ đề xuất tên thư mục và hỏi bạn xác nhận. Các skill sau tự tìm đúng thư mục đó.

> Các file `.memlog.md` là nhật ký làm việc của skill. **Không cần đọc và không được xóa**, vì skill dùng chúng để làm tiếp phiên dang dở.

---

## 8. Bảng tra nhanh

| Tôi muốn… | Gõ | Bước |
|---|---|---|
| Nghĩ nhiều hướng giải pháp | `Brainstorm giúp tôi …` | 1.1 |
| Xem đối thủ làm thế nào | `Nghiên cứu đối thủ … về …` | 1.2 |
| Viết giải pháp sơ bộ | `Viết giải pháp sơ bộ cho …` | 1.3 |
| Sửa brief sau họp | `Cập nhật brief … : <thay đổi>` | 1.3 |
| Xem thay đổi ảnh hưởng tới đâu | `Đánh giá ảnh hưởng của <file brief>` | 1.4 |
| Vẽ luồng + wireframe trắng đen | `/ux Vẽ luồng và wireframe trắng đen cho …` | 3a |
| Lên màu trên Figma | `Chuyển wireframe <file> sang Figma: <link>` | 3b |
| Kiểm tra màn Figma | `Kiểm tra màn Figma <link> theo design system` | 3b |
| Viết SRS | `Viết SRS cho …` | 5 |
| Kiểm tra SRS | `Kiểm tra SRS …` | 5 |
| Không biết bước tiếp theo | `/help` hoặc `Bước tiếp theo nên làm gì?` | — |

---

## 9. Câu hỏi thường gặp

**Có bắt buộc chạy đủ 4 skill ở Bước 1 không?**
Không. Chỉ **product-brief** và **impact-analysis** là bắt buộc. Brainstorming và deep-recon chỉ dùng khi yêu cầu còn mơ hồ hoặc cần xem đối thủ.

**Skill hỏi nhiều quá, có cách nào nhanh hơn không?**
Có. Hãy đưa đủ tài liệu ngay từ câu đầu tiên. Với product-brief, chọn **Fast path**. Với brainstorming, chọn **Ideate for me**.

**Đang làm dở mà phải dừng thì sao?**
Cứ dừng. Lần sau gọi lại đúng skill đó, nó sẽ đề nghị làm tiếp từ chỗ dừng.

**Phạm vi thay đổi sau khi đã vẽ wireframe thì làm sao?**
Cập nhật brief trước (`Cập nhật brief …`), chạy lại impact-analysis, rồi mới sửa wireframe. **Không sửa thẳng Figma hay SRS mà bỏ qua brief**, nếu không tài liệu sẽ lệch nhau.

**Skill có xuất file HTML không?**
Không. Mọi tài liệu chỉ ở dạng Markdown (`.md`) và không được đẩy lên Confluence.
