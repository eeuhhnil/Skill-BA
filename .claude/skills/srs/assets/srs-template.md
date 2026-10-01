# Template SRS của công ty

Khung chuẩn của công ty. Giữ nguyên thứ tự và tên các mục chính (1–5). Phần chữ nghiêng trong `{…}` là hướng dẫn, xóa khi viết. File `srs.md` sinh ra có thêm YAML frontmatter (xem cuối file).

~~~markdown
# {TÊN CHỨC NĂNG}

## Lịch sử thay đổi tài liệu

| Ngày thay đổi | Vị trí thay đổi | Người viết | Mô tả thay đổi |
| :---- | :---- | :---- | :---- |
| {DD/MM/YYYY} | {Toàn bộ / mục …} | {BA} | {Tạo mới / Sửa …} |

## Tài liệu liên quan

| Tên tài liệu | Nguồn/Link |
| :---- | :---- |
| {Giải pháp sơ bộ / Phân tích ảnh hưởng / Wireframe / Figma / SRS liên quan} | {Đường dẫn} |

## 1. Tổng Quan

### 1.1 Mục đích

Chức năng {Tên chức năng} được xây dựng nhằm {mục đích}, giúp {đối tượng sử dụng} có thể {kết quả mong muốn}.

### 1.2 Đối tượng sử dụng

| Role | Mô tả |
| :---- | :---- |
| {Role} | {Vai trò và mục đích sử dụng} |

### 1.3 Phạm vi áp dụng

Áp dụng cho loại hình kinh doanh:
* {Loại hình 1}
* {Loại hình 2}

Áp dụng cho nền tảng: {Web / App / Cả hai}

### 1.4 Tổng quan luồng nghiệp vụ (Business process)

{Flowchart / BPMN — chỉ bức tranh tổng quan, chưa đi vào từng field/button.}

## 2. Yêu cầu người dùng

| US-ID | Vai trò | Mong muốn | Mục đích |
| :---- | :---- | :---- | :---- |
| US-01 | {Role} | {Mong muốn} | {Mục đích} |

{Mỗi dòng đọc được thành câu: Là **[Vai trò]**, tôi muốn **[Mong muốn]**, để **[Mục đích]**.}

## 3. Danh sách các chức năng

| FR-ID | Actor | Màn hình | Tên chức năng | Mô tả chức năng | Độ ưu tiên |
| :---- | :---- | :---- | :---- | :---- | :---- |
| FR-01 | {Tác nhân} | {Màn hình} | {Tên chức năng} | {Mô tả ngắn} | {P1/P2/P3} |

| Priority | Ý nghĩa |
| :---- | :---- |
| P1 | Bắt buộc, ảnh hưởng trực tiếp đến nghiệp vụ chính |
| P2 | Quan trọng nhưng có thể triển khai sau P1 |
| P3 | Có thể thực hiện ở phase sau |

## 4. Chi tiết các chức năng

{Mỗi FR ở mục 3 phải có một mục 4.x tương ứng.}

### 4.1. FR-01 – {Tên chức năng}

#### 4.1.1. Màn hình chức năng

{Link Figma / ảnh màn hình}

| STT | Thành phần | Tên trường | Loại control | Giá trị mặc định | Bắt buộc | Mô tả |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | {Khối} | {Tên trường} | {Textbox/Dropdown/…} | {…} | {Có/Không} | {Max length · Format · Kiểu dữ liệu · Ký tự cho phép · Nguồn dữ liệu} |

#### 4.1.2. Luồng xử lý

| Hạng mục | Mô tả |
| :---- | :---- |
| Mục đích UC | {Chức năng này dùng để làm gì} |
| Điều kiện kích hoạt | {…} |

**Main flow – Luồng chính**

| Bước | Hành động người dùng | Phản hồi hệ thống |
| :---- | :---- | :---- |
| 1 | Truy cập màn hình {X} | FE: Hiển thị màn hình {Tên màn hình} |

**Alternative flow – Luồng rẽ nhánh**

| Bước | Điều kiện | Phản hồi hệ thống |
| :---- | :---- | :---- |
| {3a} | {…} | {…} |

**Exception flow – Luồng lỗi**

| Bước | Điều kiện | Thông báo hiển thị | Phản hồi hệ thống |
| :---- | :---- | :---- | :---- |
| {3b} | {…} | "{…}" | {…} |

#### 4.1.3. Quy tắc nghiệp vụ

| BR-ID | Quy tắc nghiệp vụ |
| :---- | :---- |
| BR-{feature}-001 | {…} |

## 5. Luồng ảnh hưởng

{Chức năng này ảnh hưởng đến những chức năng nào khác — lấy từ tài liệu Phân tích ảnh hưởng nếu có.}
~~~

## Frontmatter của `srs.md`

```yaml
---
title: {Tên chức năng} — SRS
type: srs
feature: {feature-slug}
status: draft          # draft → final
version: 1
created: {YYYY-MM-DD}
updated: {YYYY-MM-DD}
inputs: []             # brief, impact, wireframe, figma, SRS cũ
confluence_page_id:    # điền khi SRS được cập nhật từ một trang Confluence có sẵn
---
```

## Ghi chú so với bản gốc của công ty

- Bản gốc đánh số trùng `4.1.1` cho cả "Màn chính chức năng" và "Luồng xử lý"; template này dùng 4.1.1 / 4.1.2 / 4.1.3.
- Bản gốc ghi "Luồng ảnh hướng" → sửa chính tả "Luồng ảnh hưởng".
- Thêm cột FR-ID ở mục 3 để nối với mục 4.x.
