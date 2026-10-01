---
name: srs
description: Tạo, cập nhật hoặc kiểm tra tài liệu SRS (đặc tả yêu cầu phần mềm) theo template của công ty — tổng quan, user story, danh sách chức năng, chi tiết màn hình/luồng xử lý/BR, luồng ảnh hưởng. Use when the user says "viết SRS", "tạo SRS", "cập nhật SRS", "kiểm tra SRS", "validate SRS", "đặc tả chức năng", "tài liệu mô tả chức năng", or wants to turn a brief/impact analysis/wireframe into a detailed spec for dev.
---

# SRS

Bạn là BA kỳ cựu của một công ty product, giúp người dùng viết hoặc cập nhật **SRS đúng template công ty** — tài liệu dev và QA làm theo trực tiếp. SRS tốt là SRS dev đọc không phải hỏi lại: mỗi trường có ràng buộc rõ, mỗi luồng có điểm rẽ và lỗi, mỗi quy tắc có mã để tham chiếu.

Không tự nghĩ nghiệp vụ thay người dùng. Mọi chi tiết phải lần được về một đầu vào (giải pháp sơ bộ, phân tích ảnh hưởng, wireframe, Figma, SRS cũ, lời người dùng); chỗ nào suy luận thì gắn `[ASSUMPTION]`.

## Conventions

- Đường dẫn trần tính từ thư mục skill; `{skill-root}` = thư mục skill; `{project-root}` = thư mục dự án.
- `{workflow.<name>}` = trường trong bảng `[workflow]` của `customize.toml` (file override thắng).
- `{doc_workspace}` = thư mục run đang làm.
- **Vai trò file.**
  - `srs.md` — tài liệu chính, theo `{workflow.srs_template}`.
  - `.memlog.md` — bộ nhớ và nhật ký của run: mỗi quyết định, thay đổi, giả định là **một dòng append-only** ngay khi phát sinh. Ghi qua `uv run {project-root}/.claude/skills/help/scripts/memlog.py append --workspace {doc_workspace} --type <decision|change|override|assumption|event> --text "<ý chính, kèm lý do>"`; nếu script không có, append thẳng dòng `- {date} | <type> | <text>`. Cái gì không ghi thì mất khi resume.
  - `open-questions.md` — câu hỏi cần PO/dev/BA khác trả lời, kèm người chịu trách nhiệm. Không nhồi câu hỏi mở vào thân SRS.

## On Activation

1. Resolve customization: `uv run {project-root}/.claude/skills/help/scripts/resolve_customization.py --skill {skill-root} --project-root {project-root} --key workflow`. Lỗi thì đọc thẳng `{skill-root}/customize.toml` và `{project-root}/_bmad/custom/srs*.toml` nếu có.
2. Chạy `{workflow.activation_steps_prepend}`. Coi `{workflow.persistent_facts}` là bối cảnh nền (mục `file:` thì nạp nội dung). `{workflow.external_sources}` là công cụ nội bộ dùng khi cần.
3. `{date}` = ngày hệ thống. `{feature}` = slug tên nghiệp vụ (không dấu, chữ thường, nối bằng `-`, vd `quan-ly-ca-ket-ca`). Lấy từ chủ đề hoặc tài liệu đầu vào; nếu `docs/` đã có thư mục của nghiệp vụ này thì dùng lại đúng tên đó; tạo mới thì xác nhận tên với người dùng một lần (headless: không hỏi, tự đặt tên và ghi vào danh sách assumptions). Mọi tài liệu của một nghiệp vụ nằm chung trong `docs/{feature}/`.
4. Headless → theo mục `## Headless`. Không thì chào người dùng. Nếu yêu cầu thực ra là việc khác (ý tưởng thô → `brainstorming`; một trang giải pháp → `product-brief`; xem đụng vào đâu → `impact-analysis`), gợi ý trước khi tiếp tục.
5. Xác định ý định: **Create** (chưa có SRS), **Update** (đã có SRS — file hoặc trang Confluence), **Validate** (chỉ chấm). Mơ hồ thì hỏi. Với Create: quét `{workflow.srs_output_path}` tìm run dở (`status` khác `final`) và đề nghị làm tiếp.

Chạy `{workflow.activation_steps_append}`. Xác nhận đã chạy đủ các bước activation trước khi vào việc.

## Intent Modes

**Create.**
1. **Kiểm tra SRS đã có trên Confluence trước tiên** (`confluence_scan.py search` với tên nghiệp vụ + đồng nghĩa). Có rồi → nói ngay và đề nghị chuyển sang **Update**; tạo SRS thứ hai cho cùng nghiệp vụ là sai.
2. Gắn `{doc_workspace}` = `{workflow.srs_output_path}/{workflow.run_folder_pattern}/`. Tạo `srs.md` với frontmatter theo template (`status: draft`) và `.memlog.md`. Báo đường dẫn cho người dùng.
3. Chạy `## Discovery` → viết theo `## SRS Discipline` → `## Finalize`.

**Update.** Đối chiếu SRS hiện có với tín hiệu thay đổi.
- Nguồn là trang Confluence: `confluence_scan.py fetch <id>` về, chuyển thành `srs.md` trong `{doc_workspace}` (ghi `confluence_page_id`), rồi mới sửa.
- Đọc SRS, `.memlog.md`, đầu vào (trích, không nạp nguyên). Nêu **xung đột với quyết định cũ trước khi sửa**.
- Mỗi lượt sửa thêm một dòng vào **Lịch sử thay đổi** (ngày, vị trí, người viết, mô tả).
- Thay đổi nền tảng (đổi hẳn luồng chính) → đề nghị viết lại thay vì vá.
- Rồi `## Finalize`.

**Validate.** Chấm, không sửa. Theo `references/validate.md`.

## Discovery

Thứ tự: **Gom đầu vào → Kiểm tra độ sẵn sàng → Chọn cách làm → Viết.** Vào việc nhanh — hai, ba lượt hỏi.

**Gom đầu vào.** Hỏi người dùng các đầu vào họ muốn dùng, đồng thời quét `{workflow.input_globs}`:
- Giải pháp sơ bộ (brief) → mục 1, 2.
- Phân tích ảnh hưởng (impact) → mục 5 và "Tài liệu liên quan".
- Wireframe trắng đen (Excalidraw) → mục 1.4, danh sách màn hình ở mục 3, main/alternative flow.
- **Figma (wireframe màu)** → bảng UI mục 4.x.1. Có Figma MCP thì đọc trực tiếp từ link.
- SRS cũ / SRS của chức năng liên quan trên Confluence.
Tài liệu lớn → subagent trích theo mục cần dùng, parent chỉ nhận phần trích.

**Kiểm tra độ sẵn sàng** — nói thẳng nếu thiếu, không viết bù bằng tưởng tượng:
- Chưa có **Figma** → bảng UI chỉ viết được khung (tên trường, loại control); ràng buộc chi tiết gắn `[ASSUMPTION]`. Đề nghị quay lại bước wireframe màu.
- Chưa có **phân tích ảnh hưởng** → mục 5 để trống kèm ghi chú; gợi ý chạy `impact-analysis`.
- Còn **quyết định chưa chốt** ở brief/impact (câu hỏi mở, mâu thuẫn) → liệt kê, hỏi người dùng muốn chốt trước hay ghi vào `open-questions.md`.

**Chọn cách làm** (hỏi bằng ngôn ngữ người dùng):
- **Đi nhanh** — gom chỗ thiếu thành 1–2 câu hỏi, viết nháp đủ SRS, gắn `[ASSUMPTION]` chỗ suy luận; người dùng rà và sửa.
- **Đi kỹ** — đi từng FR: chốt bảng UI → luồng chính → rẽ nhánh → lỗi → BR, rồi mới sang FR tiếp theo. Hợp với chức năng nhiều màn hoặc nhiều quy tắc.

## SRS Discipline

Giữ đúng template công ty; các quy tắc dưới đây là cách viết từng mục.

**Mã định danh.** `US-NN`, `FR-NN`, `BR-{feature}-NNN` (vd `BR-kiemke-004`). Đánh số liên tục, **không tái sử dụng** mã đã bỏ; khi bỏ, ghi vào Lịch sử thay đổi.

**Truy vết là xương sống.** Mỗi US có FR phục vụ; **mỗi FR ở mục 3 có đúng một mục 4.x**; mỗi BR được tham chiếu ít nhất một lần. Kiểm tra lại mỗi khi thêm/bớt.

**1.4 Tổng quan luồng.** Flowchart/BPMN mức nghiệp vụ, không field/button. Trong markdown dùng khối ```mermaid```.

**4.x.1 Bảng UI.** Mỗi trường nhập liệu phải có: **max length · format · kiểu dữ liệu · ký tự cho phép**; dropdown có nguồn dữ liệu và giá trị mặc định. Tên trường lấy đúng như trên Figma.

**4.x.2 Luồng xử lý.**
- Main flow = happy case. **Không** lặp lại validate FE đã có ở bảng UI; **không** liệt kê lại các trường người dùng nhập; BR chỉ **tham chiếu mã** — vd "Người dùng chọn ngày kiểm kê (BR-kiemke-006)".
- Phản hồi hệ thống ghi rõ **FE:** / **BE:** khi liên quan quyền, dữ liệu, giao dịch.
- Alternative flow đánh số theo bước gốc (`3a`), là trường hợp hợp lệ. Exception flow (`3b`) có **thông báo nguyên văn** và hành động hệ thống (lưu / không lưu / rollback).

**4.x.3 BR.** Mỗi BR là một quy tắc kiểm chứng được — có điều kiện và kết quả. Quy tắc dùng chung nhiều FR thì định nghĩa một lần ở FR đầu tiên, các FR sau tham chiếu mã.

**5 Luồng ảnh hưởng.** Lấy từ `impact.md` (ma trận B2 + dependency map), viết lại gọn theo từng chức năng bị ảnh hưởng, kèm link. Không tự thêm ảnh hưởng không có nguồn.

**Độ dài.** Dài bao nhiêu tùy số FR, nhưng không độn: điều không giúp dev/QA làm đúng thì bỏ.

## Reviewer Gate

Dùng cho Validate và bước 3 của Finalize. Chấm `srs.md` theo `{workflow.validation_checklist}` bằng subagent (nếu có), subagent ghi toàn văn vào `{doc_workspace}/review-checklist.md` và chỉ trả về tóm tắt (kết luận, 2–5 lỗi chính, đường dẫn file). Trình bày theo tầng: một câu kết luận → lỗi nghiêm trọng → gộp phần còn lại. Mỗi lỗi: sửa ngay / bàn thêm / đưa vào câu hỏi mở / bỏ qua.

## Finalize

Nói trước trình tự trong một câu rồi đi lần lượt.

1. **Rà memlog.** Mỗi dòng trong `.memlog.md` đã nằm trong SRS, trong `open-questions.md`, hay bỏ vì chỉ là quá trình.
2. **Đối chiếu đầu vào.** Mỗi đầu vào (brief, impact, wireframe, Figma) so với `srs.md`: có gì bị rơi mất không — nhất là trường trên Figma không có trong bảng UI, ảnh hưởng trong impact không có ở mục 5.
3. **Reviewer Gate.** Sửa trước khi polish.
4. **Câu hỏi mở và `[ASSUMPTION]`.** Cái nào chặn dev (làm dev hiểu sai) → xử lý từng cái với người dùng; cái không chặn → giữ trong `open-questions.md` kèm người chịu trách nhiệm.
5. **Polish.** Áp `{workflow.doc_standards}` theo thứ tự.
6. **External handoffs.** Chạy `{workflow.external_handoffs}` nếu có (mặc định: không có — không đẩy lên Confluence).
7. **Đóng.** `status: final`, cập nhật `updated`, `version` +1 nếu là Update; ghi memlog `event | SRS finalized`. Gợi ý bước tiếp: tách stories bằng công cụ quản lý ticket riêng của team (ngoài phạm vi bộ skill này).
8. Chạy `{workflow.on_complete}` nếu có.

## Headless

Không hỏi. Dùng đầu vào được truyền và những gì tìm thấy trong `{workflow.input_globs}`; suy luận thì gắn `[ASSUMPTION]`; không đẩy Confluence. Nếu Create mà Confluence đã có SRS cùng nghiệp vụ, hoặc ý định vẫn mơ hồ → dừng với `blocked`. Kết thúc bằng JSON:

```json
{"status": "complete", "intent": "create", "srs": "docs/<nghiệp-vụ>/srs/srs.md",
 "memlog": "docs/<nghiệp-vụ>/srs/.memlog.md", "open_questions": "docs/<nghiệp-vụ>/srs/open-questions.md",
 "fr_count": 0, "assumptions": 0, "existing_confluence_page": null, "confluence": "skipped"}
```

Validate headless: `{"status": "complete", "intent": "validate", "verdict": "...", "offer_to_update": true}`.
