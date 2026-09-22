# Foundations của file Figma EP (dựng bởi easypos-design, 22/09/2026)

Dùng lại khi vẽ màn mới trong file EP. ID dạng `1159:xxx`. Style chữ: luôn dùng styleId (có style rác trùng tên).

# Figma file EP — IDs
pages: Page1 0:1 · Foundations 1159:740 · Kiểm kê kho 1159:741
icons (component id / vector id):
24: LayoutGrid 897/895 ShoppingCart 905/903 Package 914/912 Bookmark 920/918 TicketPercent 929/927 Users 938/936 Layers 946/944 ArrowLeftRight 955/953 ChartColumn 964/962 CreditCard 971/969 Home 978/976 Settings 985/983
20: ShoppingCart 993/991 Bell 1000/998 Menu 1008/1006 ChevronDown 1014/1012 Plus 1021/1019 FileUp 1030/1028 FileDown 1039/1037 Search 1046/1044
18: SquarePen 1053/1051 Trash2 1063/1061 Eye 1070/1068 Printer 1078/1076 Calendar 1087/1085 ChevronDown 1093/1091
16: ChevronLeft 1099/1097 ChevronRight 1105/1103
48: ClipboardList 1116/1114
(all prefixed 1159:)
text styles (USE styleId — names have junk duplicates; ids are "S:<hash>,"):
H1 3125b0e03b3c8dca70c3a3ca65be9e4ac70e835a · H5 24b521a144835011913454f5b8e06e4cffd7f6fa · H6 acbbafea994bb9e93c8b63d76eed64981c263293
ModalTitle 1032b1e9eba91fdeff317f6e7411b7523bf7a179 · Brand 2e965a6cc642da9a959018e481bbb7eb7144b91e
Title/lg 7f03cc394a8917d126376d942ab509bc56150808 · md 4ae8c313aefda0f571df4199280d7e4b332345d0 · sm 2a68f7051fd38417a7080668bdd5853adc95dc26 · xs 35d0de16ae2765325fb9ff613f98540af66cd6f6
Body/lg f922a7254b57d21c4230495421c4a6074f909b9c · md 41cfa0e33206c28c8de282dae1706cd0a417449a · sm 57d5a5155e3b2aa264b0cb171536a97513804bfd
Label ba964cbfed3f2c1fe12655fc0e591a7fe9b60ad1 · Caption 38548aa4322c8234094b90464cbd7f951864dc8f
Button/lg e49443c6e004626179aae6d6cc69a5fbba949a9b · md 8c33d47e7b0b8563b66315f0ac8e088986349d11
Number/table 5d45f8384fb49828685bb1ea644d2e09ab059137 · sm a5aa7c1b5426213f88f6de7f0e141a939fe798c0 · body e6cfe323def9443614049f5a383ba176b01ac9bf
TEXT recipe: create TEXT → applyTextStyle{styleId} → modify{textAutoResize:"WIDTH_AND_HEIGHT",layoutSizingHorizontal:"HUG",layoutSizingVertical:"HUG"}
components: Button/Primary/L 1159:1121 (icon inst 1118, text 1120) · Button/Secondary/L 1159:1126 (icon 1123, text 1125). props Label, Leading icon, Icon
components: Input/Search 1151 (prop Placeholder) · Input/Date range 1156 (Value) · Select 1161 (Value) · Select/S 1166 (Value)
Tag/Amber 1169 · Tag/Green 1172 (Label) · IconButton Edit 1176 Delete 1180 View 1184 Print 1188
Pager/Page 1191 (Page) · Pager/Page/Active 1194 · Pager/Prev 1198 · Pager/Next 1202
Brand/Mark 1208 · Rail/Item 1212 · Rail/Item/Active 1216 · Rail 1268 (item instances 1220..1264 step 4; Kho = 1244) · Top bar/Quản lý 1291

Màn đã vẽ: 01 Danh sách phiếu kiểm kê · Mặc định 1159:1292 · Trống 1159:1667 (page Kiểm kê kho)
