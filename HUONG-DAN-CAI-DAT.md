# Hướng dẫn cài đặt bộ skill BA

> Dành cho BA và PO dùng bộ skill lần đầu, kể cả **máy mới chưa cài gì**.
> Làm lần lượt từ Bước 1 đến Bước 8. Tổng thời gian khoảng **30–45 phút**, chỉ làm một lần cho mỗi máy.
> Cài xong, xem [README.md](README.md) để biết cách dùng skill trong từng bước của quy trình BA.

---

## Cần chuẩn bị trước

| Thứ cần có | Để làm gì | Ghi chú |
|---|---|---|
| Tài khoản **Claude** trả phí (Pro, Max, Team hoặc Enterprise) | Đăng nhập Claude Code |  |
| Tài khoản **GitHub** | Tải bộ skill | Repo riêng tư thì cần được mời vào repo trước |
| Tài khoản **Confluence** công ty | Skill đọc tài liệu cũ trên Confluence | Đăng nhập được `https://confluence-sds.softdreams.vn:8090` |
| **Figma Desktop** | Chỉ cần nếu bạn vẽ màn hình lên Figma (skill `easypos-design`) | Bản web của Figma **không dùng được** |ß

**Cách mở cửa sổ gõ lệnh** (cần ở nhiều bước bên dưới):
- **macOS:** nhấn `Cmd + Space`, gõ `Terminal`, nhấn Enter.
- **Windows:** nhấn phím `Windows`, gõ `PowerShell`, nhấn Enter.ß

Mỗi lệnh trong hướng dẫn này: copy nguyên dòng, dán vào cửa sổ trên, nhấn Enter, đợi chạy xong rồi mới gõ lệnh tiếp theo.

---

## Bước 1. Tải bộ skill về máy

Đường dẫn repo: **https://github.com/eeuhhnil/Skill-BA**

Chọn **một** trong hai cách.

### Cách A: Tải file ZIP (dễ nhất, không cần cài gì)

1. Mở đường dẫn repo ở trên, đăng nhập GitHub nếu được hỏi.
2. Bấm nút xanh **`<> Code`** → **Download ZIP**.
3. Giải nén file vừa tải (macOS: bấm đúp; Windows: chuột phải → **Extract All**).
4. Đổi tên thư mục giải nén từ `Skill-BA-main` thành `Skill-BA`, rồi chuyển vào chỗ dễ tìm, ví dụ `Documents`.

> Hạn chế: khi bộ skill có bản mới, bạn phải tải lại ZIP (xem mục "Cập nhật bộ skill" ở cuối).

### Cách B: Dùng Git (khuyên dùng, cập nhật bằng một lệnh)

1. Cài Git:
   - **macOS:** gõ lệnh dưới, bấm **Install** ở cửa sổ hiện ra, đợi cài xong.
     ```
     xcode-select --install
     ```
   - **Windows:** tải và cài [Git for Windows](https://git-scm.com/download/win), bấm **Next** giữ nguyên mọi lựa chọn mặc định.
2. Đóng cửa sổ gõ lệnh, mở lại, rồi tải repo về thư mục `Documents`:
   ```
   cd ~/Documents
   git clone https://github.com/eeuhhnil/Skill-BA.git
   ```
   Nếu được hỏi đăng nhập, làm theo cửa sổ đăng nhập GitHub hiện ra.

> ⚠️ **Người dùng Windows nên cài Git dù chọn cách A**, vì Claude Code trên Windows cần Git để chạy.

### Kiểm tra

Trong thư mục `Skill-BA` phải có: `README.md`, `HUONG-DAN-CAI-DAT.md`, thư mục `tools`, file `.mcp.json` và thư mục `.claude`. Thư mục `docs` chưa có cũng không sao, skill sẽ tự tạo khi bạn làm nghiệp vụ đầu tiên.

> `.mcp.json` và `.claude` là **file/thư mục ẩn**. Để thấy chúng: macOS nhấn `Cmd + Shift + .` trong Finder; Windows bật **View → Show → Hidden items** trong File Explorer. Không thấy chúng không có nghĩa là thiếu, chỉ là đang bị ẩn.

---

## Bước 2. Cài Visual Studio Code

1. Tải tại **https://code.visualstudio.com** và cài như phần mềm bình thường.
2. **macOS:** kéo `Visual Studio Code` vào thư mục **Applications**.

---

## Bước 3. Cài Claude Code và đăng nhập

1. Mở VS Code.
2. Bấm biểu tượng **Extensions** ở thanh bên trái (hình 4 ô vuông), hoặc nhấn `Cmd + Shift + X` (macOS) / `Ctrl + Shift + X` (Windows).
3. Tìm **Claude Code**, chọn extension của nhà phát hành **Anthropic**, bấm **Install**.
4. Bấm biểu tượng Claude (hình ngôi sao cam) xuất hiện ở thanh bên hoặc góc trên bên phải.
5. Chọn đăng nhập bằng tài khoản Claude, làm theo trang đăng nhập mở ra trên trình duyệt, rồi quay lại VS Code.

---

## Bước 4. Cài uv (để chạy công cụ đọc Confluence)

`uv` tự cài Python và các thư viện cần thiết. Bạn **không cần** tự cài Python.

- **macOS:**
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows:**
  ```
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

**Đóng cửa sổ gõ lệnh, mở lại**, rồi kiểm tra:
```
uv --version
```
Hiện ra dạng `uv 0.x.x` là được.

---

## Bước 5. Cài Node.js (để kết nối Figma) - bước này có thể bỏ qua vì không cần dùng figma

1. Tải bản **LTS** tại **https://nodejs.org** và cài, giữ nguyên mọi lựa chọn mặc định.
2. Đóng cửa sổ gõ lệnh, mở lại, rồi kiểm tra:
   ```
   node -v
   npx -v
   ```
   Cả hai lệnh đều hiện ra số phiên bản là được.

---

## Bước 6. Lấy token Confluence và lưu vào máy

Skill cần token để **đọc** tài liệu trên Confluence. Skill không bao giờ sửa hay đẩy gì lên Confluence.

### 6.1. Tạo token

1. Đăng nhập `https://confluence-sds.softdreams.vn:8090`.
2. Bấm **ảnh đại diện** ở góc trên bên phải → **Profile**.
3. Ở menu bên trái, chọn **Personal Access Tokens** → **Create token**.
4. Đặt tên, ví dụ `claude-code`, rồi bấm **Create**.
5. **Copy token ngay.** Confluence chỉ hiện token một lần, đóng cửa sổ là không xem lại được.
<img width="720" height="401" alt="image" src="https://github.com/user-attachments/assets/de09a4ac-7562-4c16-b962-6840ffa4eb9f" />

### 6.2. Lưu token vào máy

Thay `DAN_TOKEN_VAO_DAY` bằng token vừa copy, **giữ nguyên các dấu nháy**.

- **macOS:**
  ```
  echo 'export CONFLUENCE_PAT="DAN_TOKEN_VAO_DAY"' >> ~/.zshrc
  ```
- **Windows:**
  ```
  setx CONFLUENCE_PAT "DAN_TOKEN_VAO_DAY"
  ```

**Đóng cửa sổ gõ lệnh, mở lại**, rồi kiểm tra (lệnh chỉ in 4 ký tự đầu để không lộ token):
- **macOS:** `echo ${CONFLUENCE_PAT:0:4}`
- **Windows:** `$env:CONFLUENCE_PAT.Substring(0,4)`

Hiện ra 4 ký tự là đã lưu được.

> ⚠️ **Không** dán token vào chat với Claude, **không** ghi token vào file nào trong thư mục `Skill-BA`. Các file đó có thể bị đẩy lên GitHub và lộ token.

---
### 6.3. Khai báo space Confluence của nhóm bạn

Bộ skill đang để mặc định space **EP** (space của nhóm EasyPOS). Nếu bạn ở nhóm khác, đổi sang space của nhóm mình để skill đọc đúng tài liệu.

**Tìm key space của nhóm:** mở một trang bất kỳ trong space của nhóm trên Confluence và nhìn đường dẫn. Key là phần nằm ngay sau `/spaces/`:

```
https://....../spaces/EP/pages/..../EasyPos
                                                 ^^
                                                 key = EP
```

Đường dẫn dạng cũ thì key nằm sau `/display/` (`.../display/EP/...`) hoặc sau `spaceKey=` (`...spaceKey=EP`).

**Sửa key ở 3 chỗ** trong thư mục `Skill-BA` (mở bằng VS Code hoặc Notepad/TextEdit). Thay `EP` bằng key của nhóm bạn, **viết hoa đúng như trên đường dẫn**:

| File | Dòng cần sửa | Ví dụ nhóm có key `ET` |
|---|---|---|
| `.mcp.json` | `"CONFLUENCE_SPACES_FILTER": "EP",` | `"CONFLUENCE_SPACES_FILTER": "ET",` |

Nhóm cần đọc nhiều space cùng lúc thì ở `.mcp.json` ghi các key cách nhau bằng dấu phẩy, **viết liền, không có dấu cách**, ví dụ `"ET,EP"`. Hai file còn lại chỉ ghi space chính của nhóm.

## Bước 7. Mở bộ skill trong VS Code và kiểm tra kết nối

1. **Thoát hẳn VS Code** để nó nhận token vừa lưu: macOS nhấn `Cmd + Q`; Windows đóng tất cả cửa sổ VS Code.
2. Mở lại VS Code → **File → Open Folder…** → chọn đúng thư mục **`Skill-BA`**.
   Phải mở **đúng thư mục gốc**, tức thư mục chứa `README.md`, không mở thư mục con bên trong.
3. Nếu VS Code hỏi **Do you trust the authors of the files in this folder?**, chọn **Yes, I trust the authors**.
4. Mở Claude Code (biểu tượng ngôi sao cam).
5. Nếu Claude Code hỏi có dùng các **MCP server** của project không (`confluence`, `figma-ui`), chọn **đồng ý**.
6. Gõ vào ô chat của Claude Code:
   ```
   /mcp
   ```
   Kết quả đúng: `confluence` hiện trạng thái đã kết nối (connected).
   `figma-ui` có thể báo chưa kết nối với Figma cho tới khi bạn làm Bước 8. Như vậy là bình thường.

> VS Code có thể hiện cảnh báo vàng trong `.mcp.json` dạng *Variable `CONFLUENCE_PAT` not found, did you mean `${lineNumber}`*. Đây chỉ là cảnh báo của trình soạn thảo, **bỏ qua được**, Claude Code vẫn đọc đúng token.

---

## Bước 8. Kết nối Figma (chỉ khi cần vẽ màn hình lên Figma)

Bỏ qua bước này nếu bạn không dùng skill `easypos-design`.

1. Cài **Figma Desktop** tại **https://www.figma.com/downloads** và đăng nhập.
2. Tải plugin cầu nối: **[plugin.zip](https://github.com/TranHoaiHung/figma-ui-mcp/raw/main/plugin.zip)**, giải nén vào một chỗ cố định, ví dụ `Documents/figma-plugin`. Đừng xoá thư mục này sau khi cài.
3. Trong Figma Desktop, mở file thiết kế → menu **Plugins → Development → Import plugin from manifest…** → chọn file `manifest.json` trong thư mục vừa giải nén.
4. Mỗi lần muốn Claude vẽ lên Figma: mở file thiết kế, chạy **Plugins → Development → Figma UI MCP Bridge**. Cửa sổ plugin hiện **chấm xanh** là đã kết nối.
5. Kiểm tra: gõ vào Claude Code `Kiểm tra kết nối figma-ui`. Claude sẽ trả về tên file Figma đang mở.

---

## Kiểm tra lần cuối

Gõ vào Claude Code:
```
/help
```
Claude giới thiệu các skill và gợi ý bước tiếp theo là bạn đã cài xong. Tiếp theo, đọc [README.md](README.md) để biết nên gọi skill nào ở bước nào của quy trình BA.

---

## Cập nhật bộ skill khi có bản mới

- **Nếu cài bằng Git (Cách B):** mở cửa sổ gõ lệnh và chạy
  ```
  cd ~/Documents/Skill-BA
  git pull
  ```
- **Nếu tải ZIP (Cách A):** tải ZIP mới như Bước 1, rồi **chép thư mục `docs` từ bản cũ sang bản mới** trước khi xoá bản cũ. Thư mục `docs` chứa toàn bộ tài liệu bạn đã làm.

Sau khi cập nhật, thoát hẳn VS Code rồi mở lại.

---
ß
**Cần đổi token Confluence:**
- macOS: chạy `open -e ~/.zshrc`, sửa dòng `export CONFLUENCE_PAT=...`, lưu lại.
- Windows: chạy lại lệnh `setx` ở Bước 6.2 với token mới.

Sau đó thoát hẳn VS Code và mở lại.
