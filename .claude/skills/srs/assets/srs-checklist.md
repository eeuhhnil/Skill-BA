# Checklist chất lượng SRS

Dùng cho Validate và cho Reviewer Gate lúc Finalize. Mỗi mục: **Đạt / Chưa đạt / Không áp dụng**, kèm dòng trích dẫn khi chưa đạt.

## A. Cấu trúc
1. Đủ các mục: Lịch sử thay đổi · Tài liệu liên quan · 1. Tổng quan (1.1–1.4) · 2. Yêu cầu người dùng · 3. Danh sách chức năng · 4. Chi tiết chức năng · 5. Luồng ảnh hưởng.
2. Lịch sử thay đổi có dòng cho lần sửa hiện tại (ngày, vị trí, người viết, mô tả).
3. Tài liệu liên quan dẫn tới đầu vào thực tế (giải pháp sơ bộ, phân tích ảnh hưởng, wireframe, Figma) — link mở được.

## B. Tổng quan
4. 1.1 nêu đủ ba vế: mục đích · đối tượng · kết quả mong muốn.
5. 1.3 nêu rõ loại hình kinh doanh và nền tảng (Web / App / Cả hai).
6. 1.4 là bức tranh tổng quan — **không** chứa field/button.

## C. Truy vết
7. Mỗi US ở mục 2 đọc được thành "Là… tôi muốn… để…".
8. Mỗi US được ít nhất một FR ở mục 3 phục vụ; không có FR "mồ côi" không phục vụ US nào (hoặc có lý do).
9. **Mỗi FR ở mục 3 có đúng một mục 4.x** cùng mã và tên; không có mục 4.x thiếu FR ở mục 3.
10. Mã ổn định, không trùng: US-NN, FR-NN, BR-{feature}-NNN.
11. Độ ưu tiên chỉ dùng P1/P2/P3.

## D. Mô tả màn hình (4.x.1)
12. Mọi trường nhập liệu nêu đủ: **max length · format · kiểu dữ liệu · ký tự cho phép** (hoặc ghi rõ "không giới hạn").
13. Dropdown/combobox nêu nguồn dữ liệu và giá trị mặc định.
14. Trường bắt buộc/không bắt buộc được đánh dấu.
15. Có link Figma hoặc ảnh màn hình.

## E. Luồng xử lý (4.x.2)
16. Có Mục đích UC và Điều kiện kích hoạt.
17. Main flow là happy case, bước đánh số liên tục.
18. Main flow **không** lặp lại validate FE đã có trong bảng UI, **không** liệt kê lại các trường người dùng nhập.
19. BR chỉ được **tham chiếu bằng mã** trong luồng (vd "(BR-kiemke-003)"), không chép lại nội dung.
20. Alternative flow đánh số theo bước gốc (3a, 3b…) và là trường hợp hợp lệ.
21. Exception flow có thông báo hiển thị nguyên văn và hành động hệ thống (lưu / không lưu / rollback).
22. Phân biệt FE / BE khi phản hồi hệ thống liên quan đến kiểm tra quyền hoặc dữ liệu.

## F. Quy tắc nghiệp vụ (4.x.3)
23. Mỗi BR được tham chiếu ít nhất một lần trong luồng hoặc UI; không có mã BR được tham chiếu mà không định nghĩa.
24. BR viết thành quy tắc kiểm chứng được (có điều kiện và kết quả), không mơ hồ.

## G. Luồng ảnh hưởng (5)
25. Liệt kê chức năng bị ảnh hưởng và ảnh hưởng thế nào; khớp với tài liệu Phân tích ảnh hưởng nếu có.

## H. Nhất quán
26. Tên trường, tên màn hình, thông báo lỗi dùng thống nhất giữa bảng UI, luồng, BR.
27. Không mâu thuẫn với giải pháp sơ bộ / SRS cũ đã chốt — nếu có khác, ghi rõ trong Lịch sử thay đổi.
28. Không còn `[ASSUMPTION]` / câu hỏi mở chưa có người chịu trách nhiệm khi `status: final`.
