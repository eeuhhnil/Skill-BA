# Validate SRS

Chấm SRS theo `{workflow.validation_checklist}` và theo chính mục đích của nó. Không sửa file.

## Chuẩn bị
- Đọc `srs.md`, `.memlog.md` (nếu có) và các đầu vào trong frontmatter `inputs` — một bài chấm bỏ qua quyết định đã ghi là bài chấm nông.
- Nếu SRS có `confluence_page_id`: đọc bản trên Confluence (`uv run tools/confluence_scan.py fetch <id>`) để phát hiện chênh lệch giữa file và trang.

## Chấm
- Đi qua từng mục A–H của checklist. Mỗi mục **Chưa đạt** phải trích dòng/đoạn cụ thể.
- Truy vết: lập bảng US → FR → mục 4.x → BR; đánh dấu chỗ đứt.
- Nói rõ điều **không chấm được** (vd thiếu Figma nên không kiểm được bảng UI khớp màn hình).

## Báo cáo (trả trực tiếp trong chat, không tạo file trừ khi người dùng yêu cầu)
1. Một câu kết luận: **Sẵn sàng cho dev / Cần sửa trước khi giao / Chưa đủ để đánh giá**.
2. Các lỗi nghiêm trọng (chặn dev hiểu sai) — tối đa 5, mỗi lỗi kèm trích dẫn và đề xuất sửa.
3. Lỗi mức thấp gộp một dòng: "cùng N lỗi nhỏ: …".
4. Bảng truy vết rút gọn nếu có chỗ đứt.
5. Luôn hỏi: "Bạn có muốn mình chuyển các điểm này thành một lượt Update không?"
