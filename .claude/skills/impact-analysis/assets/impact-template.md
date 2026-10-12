# Mẫu tài liệu Phân tích ảnh hưởng

Khung đầu ra của skill. Giữ đủ các phần A–D; mục nào không có ảnh hưởng thì ghi rõ "Không ảnh hưởng — đã kiểm tra: <nguồn>" thay vì bỏ trống. Mọi nhận định phải có **nguồn** (link trang Confluence, file, hoặc "suy luận — cần xác nhận").

~~~markdown
---
title: {Tên nghiệp vụ} — Phân tích ảnh hưởng
type: impact-analysis
feature: {feature-slug}
status: draft
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
source_doc: "{đường dẫn brief/spec làm đầu vào}"
confluence_space: {space key đã quét, vd EP}
scan: "{N} trang khớp / {M} trang đã đọc; từ khóa: …"
---

# {Tên nghiệp vụ} — Phân tích ảnh hưởng

> **Tóm tắt (3–5 dòng):** thay đổi chính là gì, 3 ảnh hưởng lớn nhất, quyết định nào đang chặn.

## A. Tài liệu hiện có về chính nghiệp vụ này
{Đã có đặc tả/thiết kế nào trên Confluence chưa? Link, version, người sửa cuối. Nếu có: liệt kê điểm khác biệt với tài liệu đầu vào.}

## B1. Đánh giá tác động theo từng chiều

### Quy trình nghiệp vụ
- **Quy trình nào bị thay đổi?**
- **Bước nào bị thêm / xóa / sửa?**
- **Ai cần thay đổi cách làm việc?**

### Hệ thống / Kỹ thuật
- **Module / service nào cần sửa?**
- **API, database schema, UI nào thay đổi?**
- **Tích hợp bên ngoài nào bị ảnh hưởng?**

### Dữ liệu
- **Dữ liệu hiện tại có cần migrate không?**
- **Có thay đổi validation rules không?**
- **Báo cáo, dashboard nào bị ảnh hưởng?**

### Con người
- **Ai cần được training?**
- **Có thay đổi về quyền / roles không?**
- **Stakeholder nào cần được thông báo?**

## B2. Ma trận đánh giá tác động

| Thành phần bị ảnh hưởng | Loại tác động | Mức độ | Nỗ lực ước tính | Rủi ro | Nguồn | Ai xác nhận |
|---|---|---|---|---|---|---|
| [Tên module/quy trình] | Sửa đổi / Thêm mới / Xóa | High/Med/Low | [S/M/L/XL] | [Mô tả rủi ro] | [link] | [BA luồng / dev / PO] |

## B3. Dependency Map

```
[Thay đổi chính]
    ├── Phụ thuộc bởi: [A], [B]      ← ai dùng thứ thay đổi này sinh ra
    ├── Phụ thuộc vào: [C], [D]      ← thay đổi này đọc/cần gì
    └── Tích hợp với: [E]            ← hệ thống ngoài
```

## C. Mâu thuẫn và điểm cần quyết định
| # | Mâu thuẫn / câu hỏi | Giữa | Ai quyết | Trạng thái |
|---|---|---|---|---|

## D. Phạm vi quét
- Space, các nhánh đã loại, danh sách từ khóa (kèm đồng nghĩa).
- Trang đã đọc (link) · trang khớp nhưng bỏ qua vì không liên quan.
- Giới hạn: tài liệu có thể cũ hơn code; những gì chưa kiểm được.
~~~

## Quy ước

- **Mức độ** — High: phải sửa, không sửa thì sai nghiệp vụ/số liệu · Med: cần quyết định hoặc sửa nhỏ · Low: chỉ cần kiểm tra lại.
- **Nỗ lực S/M/L/XL** là ước lượng của BA để xếp thứ tự, **không phải estimate của dev** — ghi rõ như vậy trong tài liệu.
- **Loại tác động** chỉ dùng: Sửa đổi / Thêm mới / Xóa.
