---
name: easypos-figma
description: Vẽ hoặc hỏi về giao diện EasyPOS trên Figma bằng design system đã chọn (mặc định kit `pos` trong design-kits/) — màn hình web/mobile, userflow, state machine, prototype — hoặc trả lời câu hỏi về design system, token, component, màn hình đã có. Dùng khi người dùng nói "vẽ màn…", "thiết kế…", "vẽ lên Figma", "design system có … không", "màn … đang thế nào", hoặc gọi /easypos-figma. Gọi không kèm mô tả thì lấy wireframe Excalidraw của nghiệp vụ (docs/*/ux/**/*.excalidraw) làm đầu vào.
allowed-tools: Read, Glob, Grep, Bash, Write, AskUserQuestion, mcp__reqwise-figma__figma_status, mcp__reqwise-figma__figma_docs, mcp__reqwise-figma__figma_read, mcp__reqwise-figma__figma_write, mcp__reqwise-figma__figma_diagram, mcp__reqwise-figma__figma_rules
user-invocable: true
argument-hint: "<việc cần vẽ hoặc câu hỏi> — vd: vẽ màn Danh sách phiếu kiểm kê, web 1440. Để trống = vẽ từ wireframe Excalidraw"
---

# /easypos-figma — vẽ và hỏi trên Figma bằng design system

Trả lời người dùng bằng **tiếng Việt**. Công cụ là Reqwise Figma MCP (bản free).

## Tài liệu tham chiếu

Đường dẫn tính từ thư mục gốc project.

- **Design system:** `design-kits/<kit>/`. Mặc định kit `pos` cho EasyPOS; chọn kit ở mục 0.
  - `design-kit.md` — token, text style, component set, id từng biến thể, key, icon. File máy sinh. Đọc theo mục cần (grep `^### <Tên>`), không đọc cả file.
  - `design.md` — ghi chú viết tay: file nguồn, page chứa DS, collection token, font, bẫy riêng của file. **Đọc hết trước khi vẽ.**
- **Trong skill này** (`.claude/skills/easypos-figma/`):
  - `scripts/read_excalidraw.py` — đọc wireframe Excalidraw thành danh sách màn, phần tử, luồng, ghi chú.
  - `references/excalidraw-mapping.md` — quy ước màu của wireframe, phần tử → loại component, emoji → icon, tỉ lệ, luồng → prototype.
  - `references/microcopy.md` — giọng văn, viết hoa, định dạng tiền/ngày, dữ liệu mẫu, câu chữ dùng nguyên văn. Dùng khi điền nội dung và dữ liệu mẫu.
  - `assets/figma-log-template.md` — mẫu `figma-log.md` của nghiệp vụ.

## 0. Hỏi đầu vào (luôn làm đầu tiên)

1. **Đã có lựa chọn trước đó?** Nghiệp vụ đã có `docs/{feature}/ux/figma/figma-log.md` ghi file đích, page và kit → hỏi một câu xác nhận dùng lại, rồi sang bước 3.
2. **Hỏi một lượt** bằng AskUserQuestion. Không có giá trị mặc định cho file và page:
   - **File Figma đích:** link file muốn vẽ, và tên page muốn vẽ.
   - **Design system:** liệt kê các thư mục trong `design-kits/` (đọc dòng "Sản phẩm" trong `design.md` của từng kit làm nhãn), `pos — EasyPOS` xếp đầu và gắn (Recommended); thêm lựa chọn "Dán link design system khác".
   - Người dùng dán link DS chưa có kit → đề nghị sinh kit mới vào `design-kits/<tên>/` theo mục 5. Chỉ làm khi người dùng đồng ý; không đồng ý thì dừng.
3. **Kết nối.** `figma_status`. `pluginConnected: false` → dừng, bảo người dùng mở file đích trong Figma Desktop → Plugins → Development → **Reqwise Figma MCP**, giữ cửa sổ plugin mở. Không vẽ khi chưa kết nối. Đối chiếu tên file đang mở với link người dùng đưa; lệch thì báo.
4. **File đích có phải file DS không?** So với dòng "File Figma nguồn" trong `design.md` của kit.
   - **Cùng file** → dùng id biến thể trong `design-kit.md`.
   - **Khác file** → thử import một component bằng `get_library_component({ key })` (key trong `design-kit.md`).
     - Import được → dựng bằng instance import theo key.
     - Không được (library chưa publish hoặc chưa bật) → báo người dùng và đưa hai lựa chọn: vẽ trong file DS, ở page họ chọn; hoặc vẽ ở file đích chỉ bằng token và text style, không có component. Ghi rõ lựa chọn vào báo cáo.
5. **Ghi lại** file đích, page, kit vào `docs/{feature}/ux/figma/figma-log.md` (tạo theo `assets/figma-log-template.md` nếu chưa có), để lần sau không phải hỏi lại.

Mọi lệnh sau đó truyền `file: <tên file đích>` và `page: <page đã chọn>`. Đọc DS thì dùng file và page ghi trong `design.md`.

## 1. Xác định loại yêu cầu

| Người dùng muốn | Làm |
|---|---|
| **Hỏi** (DS có component X không, token màu nào, màn Y đang ra sao) | Tra `design-kit.md` trước; chỉ đọc Figma khi kit không đủ. Đọc theo node/khung, không đọc cả trang. Trả lời ngắn, không vẽ gì. Câu hỏi chỉ về DS thì mục 0 chỉ cần chọn kit. |
| **Không có prompt** (gọi `/easypos-figma` trống, hoặc chỉ "vẽ lên Figma" mà không nói vẽ gì) | Lấy wireframe theo mục 1a, rồi đi theo mục 2. |
| **Vẽ màn hình / luồng** | Đi theo mục 2. Người dùng chỉ một file `.excalidraw` → đọc theo mục 1a. |
| **Chỉ vẽ diagram** (activity, sequence, ERD, sitemap, state, userflow) | Dùng skill `/figma-<loại>` tương ứng (có sẵn trong project này); nếu không, `figma_docs({section})` rồi `figma_diagram`. |
| **Sửa design system** | Chỉ làm khi người dùng đồng ý rõ ràng — đây là sửa hệ thống thật. Làm thử 1 component, chụp cho duyệt, rồi mới làm hàng loạt. Sau đó sinh lại `design-kit.md`. |

## 1a. Lấy đầu vào từ wireframe Excalidraw

Theo `references/excalidraw-mapping.md`: §2 màu, §3 nhận dạng phần tử, §4 emoji → icon, §5 tỉ lệ, §6 luồng → prototype.

1. **Tìm file.** Glob `docs/*/ux/**/*.excalidraw` (bản nháp có thể ở `docs/*/ux/.working/`). Có một file → xác nhận với người dùng rồi dùng. Nhiều file → hỏi bằng AskUserQuestion, file sửa gần nhất xếp đầu. Không có file nào → hỏi người dùng muốn vẽ gì; không tự nghĩ ra màn.
2. **Đọc.** `PYTHONUTF8=1 python .claude/skills/easypos-figma/scripts/read_excalidraw.py <file>`, thêm `--json` khi cần tọa độ. Thiếu `PYTHONUTF8=1` thì tiếng Việt bị vỡ trên Windows. Kết quả: danh sách màn, phần tử, luồng mũi tên, ghi chú cam. Đọc thêm `DESIGN.md` / `EXPERIENCE.md` cùng thư mục `ux/` nếu có.
3. **Hiểu phần tử** theo `excalidraw-mapping.md` §3: loại phần tử → component set trong `design-kit.md` của kit đã chọn (kit `pos` đã ghi sẵn tên). Không có component tương ứng → xử lý theo luật "thiếu component" ở mục 3.
4. **Điểm chưa chốt.** Ghi chú cam (`BRIEF KHÁC: …`) và màn có trong luồng nhưng chưa vẽ khung → liệt kê, hỏi một lần cùng các câu hỏi ở bước 2.1. Không tự chọn phương án.
5. **Ghép brief.** Danh sách màn và thứ tự lấy theo số ①②③ và mũi tên. Mũi tên nhãn xanh là nút hoặc hành động ở màn nguồn, dùng cho userflow và prototype (bước 2.3, 2.6). Chữ trên wireframe giữ nguyên. Wireframe chỉ quyết định bố cục và nội dung; hình thức theo design system.

## 2. Quy trình vẽ màn hình

1. **Đủ thông tin chưa?** Đầu vào từ wireframe (mục 1a) đã có danh sách màn, thứ tự, phần tử, luồng; chỉ hỏi phần wireframe không trả lời được. Cần: nền tảng (web theo kích thước chuẩn trong `design.md` / mobile), danh sách màn + thứ tự, trạng thái mỗi màn, màn tham chiếu nào trong file (nếu có), dữ liệu mẫu. Thiếu điều gì quan trọng → hỏi MỘT lần bằng AskUserQuestion. Brief đã đủ → không hỏi, vẽ luôn.
2. **Tìm màn tham chiếu** trong file đích (search_nodes theo tên tính năng hoặc tên màn cùng loại) và chụp một ảnh để giữ bố cục quen thuộc của sản phẩm. Có màn phù hợp → clone khung (sidebar, header) rồi thay nội dung. Không có → dựng khung từ component trong kit.
3. **Userflow trước** (`figma_diagram type:"userflow"`, dryRun trước). Mỗi màn có `screenId` (vd `KK1`, `TK2`) — chính là tiền tố tên artboard. Trạng thái lỗi/disabled trên cùng màn → `kind:"state"`, không phải màn mới.
4. **Dựng màn** bằng component trong kit và khối clone từ màn tham chiếu, dùng các helper ở mục 4. Mỗi màn: chụp 1 ảnh kiểm tra, sửa, rồi `layoutAudit`.
5. **Nối flow → màn**: `figma_diagram` `update:<frameId>` + `options.linkScreens:true`.
6. **Prototype**: `setReactions` ON_CLICK → NAVIGATE cho nút chính / quay lại / lựa chọn đổi màn. Không nối nút đang disabled.
7. **State machine** nếu nghiệp vụ có trường trạng thái (phiếu, đơn, dòng…).
8. **Báo cáo** (ngắn): đã vẽ gì (file, page, node id); **thiếu gì trong DS và đã xử lý thế nào** (bảng); câu hỏi nghiệp vụ brief chưa nói. Ghi vào `figma-log.md`. Không bịa dữ liệu/chức năng ngoài brief.

## 3. Luật cứng

- **Chỉ dùng component + token có sẵn**: component trong kit, khối clone từ màn tham chiếu, token của collection ghi trong `design.md`, text style của kit. Không hardcode hex khi có token.
- **Thiếu component → liệt kê cho người dùng**. Chỉ được ghép từ atom DS (icon, text style, token) khi không còn cách nào, và phải ghi rõ "phần tự ghép".
- **Không tự tạo page.** Vẽ ở vùng trống của page người dùng đã chọn: đọc `get_design_context` (sparse, depth 1) của page, lấy x lớn nhất đang dùng, đặt cách ≥ 2000px. Mỗi tính năng một cụm, có tiêu đề text phía trên.
- **Không sửa frame có sẵn** của người khác; cần sửa thì tạo bản mới cạnh bản cũ, trừ khi người dùng bảo sửa đè.
- **Không tự sửa design system** khi chưa được phép.
- Đọc nhiều node → gom trong MỘT `figma_write` và trả về bản tóm tắt; kết quả quá lớn thì để tool lưu ra file rồi xử lý bằng node.

## 4. Helper (dán vào đầu mỗi `figma_write`)

Id biến thể truyền vào lấy từ `design-kit.md`; tên lớp text (`Label`, `Hint text`…) xem mục "Text layers" của component trong kit.

```js
const setTextByName = async (rootId, name, value, nth = 0) => {
  const r = await figma.searchNodes({ query: name, nodeId: rootId, types: ["TEXT"], limit: 40 });
  const hits = (r.nodes ?? r).filter(n => n.name === name);
  if (hits[nth]) await figma.setText(hits[nth].id, value); else console.warn("no text " + name);
};
const hideByName = async (rootId, name, type) => {
  const r = await figma.searchNodes({ query: name, nodeId: rootId, types: type ? [type] : undefined, limit: 30 });
  for (const n of (r.nodes ?? r).filter(n => n.name === name)) await figma.modify(n.id, { visible: false });
};
// nút không icon: variantId lấy từ kit, labelLayer = tên lớp text nhãn của component
const button = async (parentId, variantId, label, { w = 120, h = 40, labelLayer = "Label" } = {}) => {
  const b = await figma.create({ type: "INSTANCE", componentId: variantId, parentId });
  await setTextByName(b.id, labelLayer, label);
  for (const k of await figma.getChildren(b.id)) if (k.type === "INSTANCE") await figma.modify(k.id, { visible: false });
  await figma.resize(b.id, { w, h });
  return b.id;
};
// thẻ nền surface
const card = (name, parentId, extra = {}) => figma.create({ type: "FRAME", name, parentId, layoutAlign: "STRETCH",
  fill: "$bg-surface", cornerRadius: 8, layoutMode: "VERTICAL", itemSpacing: 16, padding: 16,
  primaryAxisSizingMode: "AUTO", counterAxisSizingMode: "FIXED", ...extra });
```

Tên token (`$bg-surface`, `$text-primary`, `$error`…) và text style (`body/md-semibold`…) ở trên theo kit `pos`; kit khác thì đổi theo `design-kit.md` của kit đó.

Kiểm tra cuối mỗi màn:
```js
const a = await figma.layoutAudit(rootId);
// bỏ qua: lớp ẩn trong instance (Vector, outline, Hint, Breadcrumbs, nút ẩn) và dòng bảng bị clip có chủ ý
```

## 5. Bẫy chung của Reqwise (đọc kỹ)

Bẫy riêng của từng file DS nằm trong `design.md` của kit.

- **`setText` để "dò font" sẽ âm thầm đổi font thiếu sang Inter.** Muốn biết font: `getDesignContext({nodeId, detail:"design", depth:0}).tree.typography.fontName`.
- **Tạo instance lỗi `unloaded font …` vẫn để lại instance mồ côi ở (0,0)** của page → sau khi thử, quét con cấp 1 của page tìm INSTANCE tại (0,0) và xóa.
- **`clone().childMap` đôi khi thiếu id lồng sâu** → nếu `childMap[x]` là undefined, tìm lại bằng `searchNodes` theo tên trong bản clone; đừng truyền null vào delete.
- **Không đổi được `layoutMode` của frame bên trong instance** (override bị bỏ qua).
- **Clone chỉ chạy trong cùng file** — màn tham chiếu phải nằm trong file đích.
- Figma thỉnh thoảng mất mạng giữa lệnh ("Unable to establish connection") → kiểm tra phần đã tạo, xóa phần dở, chạy lại từ đó.

## 6. Sinh kit / khi DS thay đổi

DS mới hoặc người dùng báo đã sửa DS → sinh kit: mở file DS, quét từng khung component trên page chứa DS (`scanNodesByTypes` theo khung, không quét cả page), ghi `design-kits/<tên>/design-kit.md` (token, text style, component set kèm key và id biến thể, text layer, icon). DS mới thì tạo thêm `design.md` theo mẫu `design-kits/pos/design.md` và hỏi người dùng phần "Nguồn". Không sửa tay `design-kit.md`; ghi chú của người để ở `design.md`.
