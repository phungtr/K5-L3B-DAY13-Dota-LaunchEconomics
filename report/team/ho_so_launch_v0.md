# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Dota · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`) = 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ). Phạm vi pilot `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu đ/tháng thành **4.599 đ** ở 45.000 yêu cầu/tháng, **5.784 đ** nếu khối lượng còn một nửa (`simulated`). Nguồn: [bang_chi_phi.md](bang_chi_phi.md) A2, A4 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: **+51,8%** (6.787 đ) · 2. Tỉ lệ xem lại ×2: **+40,7%** (6.292 đ) · 3. Lương +25%: **+23,1%** (5.506 đ). Giá token ×2 chỉ +5,6% (`simulated`). Nguồn: B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống, cộng 222 ca nhân viên làm thay: 7.037.585 ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (`simulated`). Theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` **1,88×** (`simulated`). **Con số bất lợi:** xem lại 100% tuần đầu thì lên **0,98×** (9 phút làm lại theo đề) đến **1,04×** (phút làm lại trong dữ liệu), không còn tiết kiệm (`simulated`). Nguồn: A3, B3, B4 | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chờ E1 trong [chi_so.md](chi_so.md) | Chưa | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Chờ CP3 trong [bang_loi.md](bang_loi.md) | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chờ CP4 trong [pilot_plan.yaml](pilot_plan.yaml) | Chưa | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Chờ E2 trong [chi_so.md](chi_so.md) | Chưa | PM trợ lý hoàn phí |

**Đề xuất:** *(bản nháp, chốt lúc 16:55 khi đủ mục 4–7)* Go có điều kiện cho pilot chỉ gồm `noi_dia` + `hang_nang`.

- Loại `quoc_te` (1,88×, thành công 27,3%, chạy lại không giúp: lần 1 đúng 30,0%, lần 3 chỉ 2,2%) và `doi_tac` (0,85×, có điều khoản riêng) khỏi phạm vi (`simulated`). Phụ trách: PM trợ lý hoàn phí. Kiểm tra: trước ngày bắt đầu pilot.
- Có lộ trình giảm xem lại theo bậc, vì xem lại 100% làm chi phí lên 0,98–1,04× (`simulated`). Phụ trách: Trưởng nhóm CSKH. Kiểm tra: cuối bước rollout 0.25.
- Thay hai cột phút `simulated` bằng phút đo thật từ event `nhan_vien_xem_lai`, `nhan_vien_lam_lai_xong`. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: cuối tuần 1 của pilot.
- *(Bổ sung sau CP3: các lỗi hệ thống phải sửa trước ngày bắt đầu. Sau CP4: mức chênh chấp nhận được và power, ngày quyết định khớp `decision_date`.)*
