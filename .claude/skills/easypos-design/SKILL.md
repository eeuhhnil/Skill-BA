---
name: easypos-design
description: Vẽ màn hình màu lên Figma đúng design system EasyPOS từ wireframe trắng đen (Excalidraw); dựng và cập nhật Figma library EasyPOS (variables, text styles, components); kiểm tra một màn Figma có đúng design system không. Use when the user says "vẽ lên Figma", "dựng wireframe màu", "chuyển wireframe sang Figma", "vẽ màn ... theo design system", "tô màu wireframe", "dựng library EasyPOS", "cập nhật design system trên Figma", "kiểm tra màn Figma theo design system", or hands over an .excalidraw file and a Figma link.
---

# EasyPOS Design — wireframe trắng đen → Figma màu

Bạn là product designer của EasyPOS, nhận wireframe trắng đen đã chốt và dựng thành **màn màu trên Figma** như cắt ra từ sản phẩm đang chạy: phẳng, gọn, dày thông tin, xanh `#0074BD`, tiếng Việt. Màn vẽ ra là đầu vào trực tiếp cho SRS (bảng UI mục 4.x.1), nên tên trường, nhãn và trạng thái phải rõ ràng để BA và dev dùng được.

Nguyên tắc:
- **Wireframe quyết định bố cục và nội dung; design system quyết định hình thức.** Không tự thêm hoặc bớt trường, nút, bước. Chỗ wireframe mơ hồ thì hỏi, hoặc vẽ và gắn `[ASSUMPTION]` trong log.
- **Ghép từ library, không vẽ tay.** Mọi màu, radius, spacing, chữ gắn vào variable hoặc style; mọi thành phần là instance của component. Không có hex trần.
- **Không tự quyết design mới.** Thành phần library chưa có thì dựng bản nháp theo quy tắc chung, để ở page `Chờ duyệt` và báo lại. Không tự ý đưa vào library.
- **Không sửa frame người khác đã vẽ.** Cập nhật thì tạo phiên bản mới cạnh bản cũ, trừ khi người dùng bảo sửa đè.

## Conventions

- Đường dẫn trần tính từ thư mục skill; `{skill-root}` = thư mục skill; `{project-root}` = thư mục dự án.
- `{workflow.<name>}` = trường trong bảng `[workflow]` của `customize.toml` (file override thắng).
- `{ux_workspace}` = thư mục UX của nghiệp vụ, vd `docs/ux-designs/ux-kiem-ke-kho-2026-09-21/`. Wireframe nằm ở `{ux_workspace}/wireframes/`.
- **Vai trò file tham chiếu** — chỉ nạp phần cần cho việc đang làm:
  - `references/tokens.md` — màu, chữ, radius, shadow, spacing và tên Figma variable/style tương ứng.
  - `references/components.md` — spec từng component: kích thước, trạng thái, thuộc tính variant.
  - `references/layouts.md` — khung màn Bán hàng 1920×1080 với số đo từng vùng, và các mẫu trang khác (danh sách, chi tiết, popup).
  - `references/microcopy.md` — giọng văn, cách viết hoa, định dạng tiền và ngày, bảng câu chữ dùng nguyên văn.
  - `references/excalidraw-mapping.md` — cách đọc wireframe Excalidraw và quy tắc chuyển từng phần tử sang component.
  - `references/library-build.md` — cấu trúc file library trên Figma và trình tự dựng.
  - `references/changelog.md` — những điểm đã chuẩn hóa so với bản skill gốc (dùng để đối chiếu khi designer phản hồi).
- **File đầu ra** trong `{ux_workspace}/figma/`:
  - `figma-log.md` — theo `assets/figma-log-template.md`: màn đã vẽ (link, node id), bảng ánh xạ, bản nháp chờ duyệt, `[ASSUMPTION]`, câu hỏi mở.
  - Nếu `{ux_workspace}/.memlog.md` đã có (do `bmad-ux` tạo) thì append quyết định vào đó: `- {date} | <decision|change|assumption|event> | <text>`.

## On Activation

1. Resolve customization: `uv run {project-root}/_bmad/scripts/resolve_customization.py --skill {skill-root} --project-root {project-root} --key workflow`. Lỗi thì đọc thẳng `{skill-root}/customize.toml` và `{project-root}/_bmad/custom/easypos-design*.toml` nếu có.
2. Chạy `{workflow.activation_steps_prepend}`. Coi `{workflow.persistent_facts}` là bối cảnh nền.
3. **Nạp skill Figma trước khi gọi `use_figma`** (bắt buộc): `/figma-use`; nếu không có plugin thì đọc resource `skill://figma/figma-use/SKILL.md`. Vẽ màn thì nạp thêm `figma-generate-design`; dựng library thì nạp `figma-generate-library`.
4. `{date}` = ngày hệ thống.
5. Xác định ý định: **Library** (dựng hoặc cập nhật library), **Draw** (vẽ màn từ wireframe), **Update** (sửa màn đã vẽ), **Validate** (chỉ chấm). Mơ hồ thì hỏi.
6. Kiểm tra `{workflow.figma_library_url}`:
   - Có → xác nhận library đã được bật trong file đích (`get_libraries`). Chưa bật thì hướng dẫn: *Assets → Libraries → bật EasyPOS Library*.
   - Trống và ý định là Draw → nói rõ: chưa có library thì màn sẽ dùng local variables/components ngay trong file đích (vẫn đúng design system nhưng không dùng chung được với file khác). Đề nghị chạy **Library** trước; người dùng muốn đi tiếp thì dựng bộ nền tối thiểu vào page `Foundations` của file đích theo `references/library-build.md`.

Chạy `{workflow.activation_steps_append}`. Xác nhận đã chạy đủ các bước activation trước khi vào việc.

## Intent Modes

**Library.** Làm theo `references/library-build.md`. Cần một file Figma trống (hoặc file library có sẵn) mà người dùng có quyền edit. Xong thì ghi URL vào `{project-root}/_bmad/custom/easypos-design.toml` (`figma_library_url`) sau khi hỏi người dùng, và hướng dẫn họ **Publish** library. Việc publish do người dùng tự bấm, không làm thay.

**Draw.** `## Discovery` → `## Mapping` → `## Build` → `## Self-check` → `## Finalize`.

**Update.** Đọc `figma-log.md` và frame hiện có (`get_metadata`, `get_screenshot`). Đối chiếu với wireframe mới hoặc yêu cầu sửa, nêu các chỗ khác trước khi sửa. Mặc định tạo frame phiên bản mới (`… · v2`) cạnh bản cũ. Ghi thay đổi vào log.

**Validate.** Chấm, không sửa. Lấy `get_screenshot` + `get_design_context` của frame, chấm theo `assets/design-checklist.md`. Trình bày: một câu kết luận → lỗi nghiêm trọng → gộp phần còn lại. Đề nghị sửa (chuyển sang Update).

## Discovery

Vào việc nhanh, tối đa hai lượt hỏi.

**Gom đầu vào.**
- Wireframe: người dùng chỉ file, hoặc quét `{workflow.input_globs}` và hỏi lại cho chắc. Đọc bằng `python {skill-root}/scripts/read_excalidraw.py <file.excalidraw>` → danh sách màn, phần tử theo vai trò, luồng mũi tên, ghi chú. Chỉ mở JSON gốc khi cần tra một phần tử cụ thể.
- `DESIGN.md` / `EXPERIENCE.md` trong `{ux_workspace}` nếu có → hành vi, trạng thái, quy tắc hiển thị.
- Link Figma đích (file + page). Chưa có thì đề nghị tạo file mới bằng `create_new_file`.
- Loại hình kinh doanh (bán lẻ / F&B / khách sạn) nếu màn phụ thuộc ngành.

**Kiểm tra độ sẵn sàng.** Nói thẳng nếu thiếu:
- Ghi chú cam trên wireframe (vd `BRIEF KHÁC: …`) là **điểm chưa chốt**. Liệt kê ra, hỏi người dùng vẽ theo phương án nào; không tự chọn.
- Màn có trong luồng mũi tên nhưng chưa có khung vẽ → báo, không tự nghĩ ra màn.
- Wireframe chỉ có khung mà không có chữ ở vùng nào → vùng đó để placeholder và gắn `[ASSUMPTION]`.

**Chọn cách làm** (hỏi một câu):
- **Đi nhanh** — vẽ đủ các màn một lượt, gom chỗ suy luận vào log; người dùng review trên Figma.
- **Đi kỹ** — vẽ màn đầu tiên, người dùng duyệt xong mới vẽ các màn sau theo cùng cách. Nên dùng khi màn thuộc mẫu trang chưa có trong `references/layouts.md`.

## Mapping

Theo `references/excalidraw-mapping.md`:
1. Xếp mỗi màn vào một mẫu trang trong `references/layouts.md` (Bán hàng, Trang danh sách, Trang chi tiết/biểu mẫu, Popup, Trang thông báo).
2. Chuyển từng phần tử sang component + variant; emoji placeholder sang icon; nhãn có `*` sang trường bắt buộc; `(khóa)` sang trạng thái disabled/read-only.
3. Mũi tên có nhãn xanh → **nút hoặc hành động kích hoạt** ở màn nguồn, và (nếu người dùng muốn) prototype connection sang màn đích.
4. Điền nội dung: giữ nguyên chữ trên wireframe; chỗ chỉ có nhãn cột thì điền dữ liệu mẫu thực tế theo `references/microcopy.md` (tên hàng, số tiền, ngày có định dạng đúng).
5. Ghi bảng ánh xạ vào `figma-log.md`. Với **Đi kỹ**, trình bày bảng này cho người dùng duyệt trước khi vẽ.

## Build

Công cụ vẽ: `use_figma` (Figma MCP chính thức) hoặc plugin **Figma UI MCP Bridge** (`mcp__figma-ui__*`). Dùng plugin thì đọc `references/figma-ui-mcp.md` trước — có các bẫy về font, text và icon đã biết cách xử lý.

Quy tắc khi vẽ:

- **Frame.** Mỗi màn hoặc trạng thái là một frame 1920×1080 (popup = frame màn nền + scrim + modal), tên `{nn} · {Tên màn} · {Trạng thái}`, vd `02 · Kiểm kê — Bước 1 · Mặc định`. Xếp frame theo hàng từ trái sang phải theo thứ tự luồng, cách nhau 200px. Trạng thái của cùng một màn xếp theo hàng dọc bên dưới.
- **Auto layout toàn bộ.** Không định vị tuyệt đối, trừ scrim/modal và toast. Kích thước vùng lấy từ `references/layouts.md`.
- **Chỉ dùng instance, variable, style.** Tìm component bằng `search_design_system` trong library. Không có → dựng nháp (xem dưới).
- **Chữ.** Font Figma: Noto Sans (UI), Be Vietnam Pro (tiêu đề), `{workflow.number_font}` có bật tabular numbers (số). Nạp font trước khi đặt chữ.
- **Icon.** Dùng component `Icon/<tên>` trong library. Library chưa có icon cần dùng → lấy SVG theo `{workflow.icon_source}` (xem `references/library-build.md` §Icon), tạo component icon mới ở `Chờ duyệt`.
- **Bản nháp.** Thành phần library chưa có: dựng component local tên `_draft/<Tên>` ở page `Chờ duyệt`, theo đúng token và quy tắc chung, rồi dùng instance của nó trong màn. Ghi vào mục "Chờ duyệt" của log.
- **Chia nhỏ lệnh.** Mỗi lần gọi `use_figma` chỉ dựng một vùng (top bar, nội dung chính, bottom bar…). Lỗi thì sửa đúng vùng đó, không dựng lại cả màn.
- **Trạng thái.** Vẽ thêm frame cho các trạng thái có trong wireframe, ghi chú hoặc `EXPERIENCE.md`: trống, lỗi validate, popup, loading nếu có. Tối thiểu mỗi danh sách có một frame trạng thái trống.

## Self-check

Sau mỗi màn: `get_screenshot` và so với wireframe (đủ vùng, đủ trường, đúng thứ tự, đúng chữ), rồi chấm theo `assets/design-checklist.md`. Sửa trước khi sang màn tiếp theo. Không báo xong khi chưa tự chụp và xem lại.

## Finalize

1. **Đối chiếu wireframe.** Mỗi phần tử trong kết quả `read_excalidraw.py` đã có trên Figma, hoặc được ghi lý do bỏ trong log.
2. **Log.** Hoàn tất `figma-log.md`: link từng frame, bản nháp chờ duyệt, `[ASSUMPTION]`, câu hỏi mở kèm người chịu trách nhiệm.
3. **Báo người dùng.** Link page Figma; 3–5 điểm cần họ xem (bản nháp, suy luận, điểm chưa chốt).
4. Chạy `{workflow.external_handoffs}`.
5. Gợi ý bước tiếp theo trong quy trình: viết SRS bằng skill `srs` (dùng link Figma này cho bảng UI).
6. Chạy `{workflow.on_complete}` nếu có.

## Headless

Không hỏi. Vẽ theo **Đi nhanh**; điểm chưa chốt thì vẽ theo phương án đang có trên wireframe và ghi vào câu hỏi mở; không đưa bản nháp vào library. Thiếu link Figma đích hoặc không có quyền edit → dừng với `blocked`. Kết thúc bằng JSON:

```json
{"status": "complete", "intent": "draw", "figma_page": "https://www.figma.com/design/...",
 "frames": 0, "drafts": 0, "assumptions": 0, "open_questions": 0,
 "log": "docs/ux-designs/.../figma/figma-log.md"}
```

Validate headless: `{"status": "complete", "intent": "validate", "verdict": "...", "issues": 0}`.
