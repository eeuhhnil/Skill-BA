# Checklist màn Figma EasyPOS

Dùng cho Self-check sau mỗi màn và cho Validate. Mỗi mục: **Đạt / Chưa đạt / Không áp dụng**; chưa đạt thì ghi tên layer và mô tả ngắn.

## A. Khớp wireframe
1. Đủ các vùng, trường, cột, nút như wireframe; không thêm thành phần wireframe không có (trừ trạng thái được yêu cầu).
2. Thứ tự và nhóm phần tử giữ đúng wireframe.
3. Chữ giữ nguyên văn wireframe (chỉ sửa chính tả, có ghi log).
4. Mỗi luồng ra khỏi màn có nút/link tương ứng.
5. Ghi chú cam và chú thích cho người đọc không bị vẽ thành UI.

## B. Design system
6. Mọi fill, stroke, chữ gắn variable/style; **không có hex trần** (kiểm bằng `get_design_context`).
7. Mọi thành phần là instance của library (hoặc `_draft/*` đã ghi log); không có nhóm hình vẽ tay thay component.
8. Xanh `#0074BD` là màu duy nhất cho hành động chính; mỗi vùng tối đa một nút Primary.
9. Radius thuộc thang 4/6/8/12/16/full; card nội dung chính radius 16 trên nền `surface/page`; khoảng cách giữa card 16.
10. Padding/gap thuộc lưới 4px.
11. Không gradient, texture, bóng màu, kính mờ; shadow chỉ dùng `Shadow/*`.
12. Icon cùng một bộ, đúng cỡ 24/20/18/14 theo ngữ cảnh; không emoji, không ký tự Unicode làm icon.

## C. Nội dung
13. Tiếng Việt đủ dấu, viết hoa kiểu câu; IN HOA chỉ ở tiêu đề thông báo toàn trang.
14. Tiền `5.000.000đ`, ngày `DD/MM/YYYY`; số dùng font số, căn phải trong bảng; tổng tiền đậm, xanh.
15. Dữ liệu mẫu thực tế, đa dạng (đủ các trạng thái trong cột trạng thái), không Lorem ipsum.
16. Thông báo lỗi và toast viết nguyên văn, đúng giọng văn.

## D. Bố cục và trạng thái
17. Frame 1920×1080, đặt tên `{nn} · {Tên màn} · {Trạng thái}`; kích thước vùng đúng `layouts.md`.
18. Auto layout toàn bộ (trừ scrim, modal, toast); resize frame không vỡ bố cục.
19. Chỉ vùng bảng/lưới được cuộn (clip content); không có thanh cuộn ngoài.
20. Có frame trạng thái trống cho mỗi danh sách; có trạng thái lỗi cho form có validate; có frame cho mỗi popup trong luồng.
21. Trường bắt buộc có `*`; trường khóa ở trạng thái Disabled; nút phím tắt có keycap (`F8`, `F9`) khi áp dụng.

## E. Truy vết
22. `figma-log.md` có link từng frame, bảng ánh xạ, bản nháp chờ duyệt, `[ASSUMPTION]`, câu hỏi mở.
