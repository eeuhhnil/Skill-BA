# BMad knowledge

Installed skills are grouped by their manifest's `module` key. Each module's
knowledge is read from that manifest's `knowledge` value: free-form text
saying where the module's knowledge lives or what it is. Follow it for the
module the question concerns. This document is what the `method` and
`toolbox` manifests point at; another module points elsewhere, and nothing
below describes it.

## The method and toolbox modules

This installation carries a focused BA toolkit — shaping product intent from
a raw idea through to the SRS handed to dev/QA. It does **not** include
BMad's implementation pipeline (spec/build/code-review/QA-test-gen/
retrospective); do not route toward skills that are not listed below, even if
general BMad knowledge mentions them.

### The skills and their places in the flow

Shaping and planning:

- `brainstorming` — facilitated ideation across many creative techniques.
  Good entry point for a raw idea with no shape yet.
- `deep-recon` — research to support a decision: drafts a research prompt for
  the user's own tool, or runs the research itself (market, domain,
  technical, competitive, user-voice, academic-lit).
- `product-brief` — shapes a product concept into a brief (preliminary
  business solution).
- `ux` — records user experience decisions as DESIGN.md (how it looks) and
  EXPERIENCE.md (how it works); belongs after the brief once the form factor
  is known.
- `impact-analysis` — assesses how a change touches the existing system
  (processes, systems, data, people) by scanning the company's Confluence
  documentation; ma trận tác động + dependency map.
- `srs` — turns a shaped concept (brief, and UX/impact analysis when
  relevant) into the company's SRS template — the document dev and QA work
  from directly.

Agent personas (optional):

- `agent-analyst`, `agent-dev`, `agent-pm`, `agent-ux-designer` —
  conversations with a single named perspective. No path above needs them;
  the flow skills already do this work. Offer one only when the user asks to
  talk to a specific role or wants one perspective's take without running a
  full skill.

A project environment may have a subset of these skills supporting the user's
preferred workflow.

Cross-skill routing exists only when the `help` hub skill is installed.

### How to use this toolkit

The company's BA flow: kiểm tra tài liệu đã có → brainstorming → research →
giải pháp sơ bộ (brief) → đánh giá ảnh hưởng (impact-analysis) → họp chốt →
wireframe trắng đen → wireframe màu trên Figma (qua skill riêng của dự án nếu
có cài, ví dụ `easypos-design`) → SRS → stories (tách story nằm ngoài phạm vi
bộ skill này — dùng công cụ quản lý ticket riêng của team).

- Ý tưởng còn thô, chưa có hình hài → `brainstorming`.
- Ý tưởng cần thêm bối cảnh thị trường/đối thủ/công nghệ trước khi chốt →
  `deep-recon`.
- Đã sẵn sàng chốt thành tài liệu → `product-brief` (tạo mới hoặc cập nhật).
- Giao diện/trải nghiệm người dùng là phần quan trọng của việc này → `ux`,
  sau khi đã có brief.
- Cần biết thay đổi này đụng tới đâu trong hệ thống hiện có →
  `impact-analysis`.
- Sẵn sàng viết đặc tả cho dev/QA → `srs`, sau khi đã có brief (và UX/Figma/
  impact analysis khi liên quan).

### Answering "what's next?"

Read the state before recommending: which planning artifacts exist (brief,
UX designs, impact analysis, SRS), and what the user says is done. Caution:
a file's mere presence does not prove completion — check its frontmatter
`status` and ask if unsure.

- Chưa có brief → gợi ý `brainstorming` trước nếu ý tưởng còn thô, không thì
  vào thẳng `product-brief`.
- Đã có brief, UI/UX là phần quan trọng, chưa có UX → `ux`.
- Đã có brief, chưa rõ ảnh hưởng lên hệ thống hiện có → `impact-analysis`.
- Đã có brief (kèm UX/impact analysis khi liên quan), chưa có SRS → `srs`.

A run is complete when the intent is satisfied and its chosen checks pass —
not when every skill has been traversed.

### When this document is not enough

For a method or toolbox question this section and the installed skills
cannot answer, fetch `https://docs.bmad-method.org/llms.txt` and follow the
links relevant to the question. It indexes the full BMad documentation site.
Note: the upstream source still uses the original `bmad-*` skill names and
lists the full upstream skill catalog — this installation has been renamed
and pruned locally to the company's chosen subset, so treat upstream mentions
of any skill not listed above as unavailable here, not as a routing option.

### Where things land

Planning documents (brief, UX designs, research, impact analysis, SRS) live
under `{planning_artifacts}`; repository guidance, if the team keeps one, at
`{project-root}/AGENTS.md`.
