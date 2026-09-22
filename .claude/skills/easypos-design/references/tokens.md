# Design tokens EasyPOS

Nguồn gốc: `EasyPos - Design system (1).fig` và các màn đang chạy. Cột **Figma** là tên variable/style trong library; khi vẽ luôn gắn vào tên này, không gõ hex.

## 1. Màu — collection `Primitives`

### Blue (màu chính, mọi hành động chính)
| Figma | Hex | Dùng cho |
|---|---|---|
| `blue/900` | `#00314F` | sâu nhất |
| `blue/800` | `#004671` | tiêu đề tối trên nền sáng |
| `blue/700` | `#005C96` | pressed; chữ trên nền tint |
| `blue/600` | `#0068AA` | hover của nút chính |
| `blue/500` ★ | `#0074BD` | **màu chính**: top bar, nút chính, link, active, tổng tiền, stepper |
| `blue/400` | `#3392CB` | icon phụ, hover icon rail |
| `blue/300` | `#66ADD9` | |
| `blue/200` | `#B0D4EB` | keycap trên nút phụ, viền chip active |
| `blue/150` | `#DCEBF6` | hover của nền tint |
| `blue/100` | `#E6F1F8` | nền tint: rail active, nút tertiary, chip active |
| `blue/50` | `#F0F7FB` | nền rất nhạt, hover rail, hộp số tiền trong popup |
| `blue/accent` | `#0767FE` | icon trên một số nút viền |

### Orange (màu phụ: tag Topping, badge trên top bar)
`orange/800 #7D451E` · `700 #A15926` · `600 #CF7331` · `500 #E37E36` ★ · `400 #E9985E` · `300 #ECA978` · `200 #F2C4A3` · `100 #F6D7C1` · `50 #FCF2EB`

### Neutral (thang xám ngả navy)
`ink #151B33` ★ (chữ chính) · `gray/800 #08062A` · `700 #0B0737` · `600 #0E0946` · `500 #0F0A4D` · `400 #3F3B71` · `300 #5E5B88` · `200 #918EAD` · `100 #B5B3C8` · `50 #E7E7ED` · `white #FFFFFF`

### Trạng thái
| Nhóm | 700 | 500 | 300 | 100 | 50 |
|---|---|---|---|---|---|
| `success` | `#1E7D45` | `#2BA45C` | — | `#C8F2D7` | `#E0FFEB` |
| `warning` | `#B7791F` | `#F0A92A` | — | `#FDEFC8` | `#FFFAE7` |
| `error` | `#BE211C` | `#EB5146` | `#FDA59B` | `#FED9D5` | `#FEF3F2` |

Teal (`#449297`) có trong file Figma gốc nhưng **không dùng** trong sản phẩm, không đưa vào library.

## 2. Màu — collection `Semantic` (alias sang Primitives)

Khi vẽ màn, ưu tiên dùng tên semantic.

| Figma | Alias | Dùng cho |
|---|---|---|
| `text/primary` | `ink` | chữ chính |
| `text/secondary` | `#455064` | nhãn, chú thích, tiêu đề cột |
| `text/tertiary` | `#545454` | nội dung phụ |
| `text/placeholder` | `#B0B0B0` | placeholder, chữ disabled |
| `text/on-primary` | `white` | chữ trên nền xanh |
| `text/link` | `blue/500` | link |
| `surface/default` | `white` | card, panel |
| `surface/page` | `#F4F6F8` | nền trang |
| `surface/subtle` | `#F7F7F7` | chip, dòng xen kẽ, nền thumbnail |
| `surface/disabled` | `gray/50` | nền control disabled |
| `border/default` | `#E6E6E6` | viền 1px mặc định |
| `border/strong` | `#DEE0E2` | viền checkbox/radio, gạch chân giá |
| `border/faint` | `#EEEEEE` | kẻ dòng bảng, viền product card |
| `action/primary` | `blue/500` | |
| `action/primary-hover` | `blue/600` | |
| `action/primary-pressed` | `blue/700` | |
| `action/tint` | `blue/100` | |
| `action/tint-hover` | `blue/150` | |
| `action/destructive` | `error/500` | |
| `focus/ring` | `blue/100` | vòng focus 3px |
| `overlay/scrim` | `rgba(10,18,35,0.45)` | nền mờ sau popup |
| `overlay/on-primary` | `white @16%` | nút trên top bar |
| `overlay/keycap-on-primary` | `white @22%` | keycap F9 trên nút chính |
| `icon/muted` | `gray/200` | icon rail, icon xóa |
| `icon/empty` | `gray/100` | icon trạng thái trống |

## 3. Chữ — text styles

Tỉ lệ dòng: tiêu đề 150% (H1 120%), body 150%, title/label 140%. Letter spacing 0.

| Style | Font | Weight | Size / line-height |
|---|---|---|---|
| `Display/H1` | Be Vietnam Pro | 600 | 64 / 77 |
| `Display/H2` | Be Vietnam Pro | 600 | 48 / 72 |
| `Display/H3` | Be Vietnam Pro | 600 | 40 / 60 |
| `Display/H4` | Be Vietnam Pro | 600 | 36 / 54 |
| `Display/H5` | Be Vietnam Pro | 600 | 24 / 36 |
| `Display/H6` | Be Vietnam Pro | 600 | 20 / 30 |
| `Display/Modal title` | Be Vietnam Pro | 700 | 22 / 32 |
| `Brand/Wordmark` | Be Vietnam Pro | 800 | 22 / 28 |
| `Title/lg` | Noto Sans | 600 | 20 / 28 |
| `Title/md` | Noto Sans | 600 | 16 / 22 |
| `Title/sm` | Noto Sans | 600 | 14 / 20 |
| `Title/xs` | Noto Sans | 600 | 12 / 16 |
| `Body/xl` | Noto Sans | 400 | 20 / 30 |
| `Body/lg` | Noto Sans | 400 | 16 / 24 — mặc định |
| `Body/md` | Noto Sans | 400 | 14 / 20 |
| `Body/sm` | Noto Sans | 400 | 12 / 18 |
| `Label` | Noto Sans | 500 | 14 / 20 |
| `Caption` | Noto Sans | 400 | 12 / 16 |
| `Button/lg` | Noto Sans | 700 | 16 / 24 |
| `Button/md` | Noto Sans | 700 | 14 / 20 |
| `Button/sm` | Noto Sans | 700 | 13 / 18 |
| `Button/action` | Noto Sans | 700 | 20 / 28 — Lưu đơn / Thanh toán ở bottom bar |
| `Number/xl` | `{number_font}` | 700 | 28 / 36 — số tiền trong popup |
| `Number/lg` | `{number_font}` | 700 | 26 / 32 — Tổng tiền hàng |
| `Number/md` | `{number_font}` | 700 | 22 / 28 |
| `Number/body` | `{number_font}` | 700 | 16 / 24 — giá trên product card |
| `Number/table` | `{number_font}` | 700 | 15 / 20 — số trong bảng |
| `Number/sm` | `{number_font}` | 600 | 13 / 18 — tồn kho, pager |

Mọi style `Number/*` bật OpenType **tabular figures** (`tnum`). Số trong bảng căn phải.

## 4. Radius — collection `Radius`

| Figma | px | Dùng cho |
|---|---|---|
| `radius/xs` | 4 | keycap, chip rất nhỏ |
| `radius/sm` | 6 | input, chip lọc, tag, stepper, nút nhỏ, pager |
| `radius/md` | 8 | nút, mục rail, nút top bar, segmented, ô tổng tiền, thumbnail |
| `radius/lg` | 12 | dropdown, popover, product card |
| `radius/xl` | 16 | card nội dung chính, popup |
| `radius/full` | 999 | badge đếm, toggle, avatar |

Không dùng giá trị ngoài bảng này.

## 5. Spacing — collection `Spacing`

Lưới 4px: `space/1 4` · `space/2 8` · `space/3 12` · `space/4 16` · `space/5 20` · `space/6 24` · `space/8 32` · `space/10 40` · `space/16 64`. Riêng padding dọc của tag/chip nhỏ được dùng `space/half 2`.

Khoảng cách giữa các card: 16. Padding trong card: 20 ngang, 16 dọc.

## 6. Chiều cao control

`24` stepper · `32` pager, nút nhỏ · `40` input, nút top bar, ô tìm kiếm · `48` nút trên order header, ô ghi chú, segmented · `56` nút xác nhận trong popup.

## 7. Hiệu ứng — effect styles

| Figma | Giá trị | Dùng cho |
|---|---|---|
| `Shadow/sm` | 0 1 2 `rgba(16,24,40,0.08)` | chip, segmented active, hover nhẹ |
| `Shadow/md` | 0 4 12 `rgba(16,24,40,0.15)` | card khi hover, popover |
| `Shadow/lg` | 0 12 32 `rgba(16,24,40,0.16)` | popup, toast |
| `Focus/ring` | spread 3 `blue/100` | control đang focus |

Không gradient, không texture, không bóng có màu, không kính mờ.
