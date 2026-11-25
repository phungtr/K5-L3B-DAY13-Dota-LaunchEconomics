# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: Dota · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ** (`simulated`) = 16,3× hoá đơn token + tool chia số yêu cầu (274,7 đ). Phạm vi pilot `noi_dia` + `hang_nang`: 3.414 đ, cộng cố định 40 triệu đ/tháng thành **4.599 đ** ở 45.000 yêu cầu/tháng, **5.784 đ** nếu khối lượng còn một nửa (`simulated`). Nguồn: [bang_chi_phi.md](bang_chi_phi.md) A2, A4 | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại ×2: **+51,8%** (6.787 đ) · 2. Tỉ lệ xem lại ×2: **+40,7%** (6.292 đ) · 3. Lương +25%: **+23,1%** (5.506 đ). Giá token ×2 chỉ +5,6% (`simulated`). Nguồn: B1, B2 | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống, cộng 222 ca nhân viên làm thay: 7.037.585 ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** của 12.000 đ (`simulated`). Theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` **1,88×** (`simulated`). **Con số bất lợi:** xem lại 100% tuần đầu thì lên **0,98×** (9 phút làm lại theo đề) đến **1,04×** (phút làm lại trong dữ liệu), không còn tiết kiệm (`simulated`). Nguồn: A3, B3, B4 | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chỉ số trong đợt chạy thử: chính **82,83%** (994/1.200) · dùng, bỏ qua gợi ý **27,12%** (48/177) · an toàn, mở lại 7 ngày **4,25%** (51/1.200). Đợt chạy thử không có đối chứng nên chưa nói được trợ lý nâng chỉ số. Thêm 2 chỉ số tự đề xuất (% nhân viên dùng thật hằng tuần; % gợi ý giữ nguyên nhưng vẫn bị mở lại); 9 event có `trace_id`, mỗi chỉ số chỉ ra được event để tính. Nguồn: [chi_so.md](chi_so.md) E1 | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 5 · Bảng lỗi và cách khắc phục | Hai người gắn nhãn độc lập, đồng thuận **16/20 = 80%**; 4 ca lệch (1, 3, 8, 13) có quy tắc phân biệt. Phân bố: Hệ thống 5 · Do người dùng 4 · Ngữ cảnh 4 · Giới hạn 4 · Ngầm 3. Bảng khắc phục đủ 5 loại (ca 14, 7, 16, 4, 5), mỗi dòng có ngưỡng đo được. Nặng nhất: ca 7 báo "đã hoàn" khi sổ cái lỗi 503, ca 20 hoàn hai lần vì thiếu khoá chống trùng. Nguồn: [bang_loi.md](bang_loi.md) | Xong, có bằng chứng | Kỹ sư backend phụ trách trợ lý hoàn phí |
| 6 · Pilot plan | Chia theo **nhân viên 20 + 20**, cả 12 depot, ngẫu nhiên phân tầng theo depot. Mức chênh **6 điểm**: n hiệu dụng 859/nhóm, DE 6,96, ≥ 299 yêu cầu mỗi người. **Con số bất lợi:** power chỉ 0,64 nếu chênh thật 5 điểm; chia theo depot chỉ đạt 300. Luật an toàn so với đối chứng (+2 điểm) kèm trần 6%, vì nền hiện tại đã 4,25%. Quyết định ngày **2027-01-08**. Nguồn: [pilot_plan.yaml](pilot_plan.yaml) | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Ba dòng rủi ro lấy số từ B1 (`simulated`): ca làm lại ×2 → **6.787 đ (+51,8%)** · tỉ lệ xem lại ×2 → **6.292 đ (+40,7%)**, xem lại 100% thì 1,04× · lương +25% → **5.506 đ (+23,1%)**. Mỗi dòng có dấu hiệu theo dõi bằng event và một vai trò phụ trách; nối với luật dừng chi phí 8.000 đ trong pilot. Nguồn: [chi_so.md](chi_so.md) E2 | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ gồm `noi_dia` + `hang_nang`, cả 12 depot, bắt đầu 2026-12-07, quyết định ngày 2027-01-08.

Lý do: trong phạm vi, chi phí 4.599 đ/việc thành công kể cả chi phí cố định = 0,38× của 12.000 đ (`simulated`); pilot có đối chứng ngẫu nhiên 20 cụm mỗi nhóm và ba luật dừng có ngưỡng, thời hạn, người có quyền dừng. Có điều kiện vì năm điểm bất lợi dưới đây, mỗi điều kiện xử lý một điểm:

- Sửa ca 7 (chỉ báo "đã hoàn" khi sổ cái trả mã xác nhận) và ca 20 (khoá chống trùng cho lệnh hoàn). Phụ trách: Kỹ sư backend phụ trách trợ lý hoàn phí. Kiểm tra: 2026-12-04, trước ngày bắt đầu.
- Loại `quoc_te` (1,88×, thành công 27,3%, chạy lại không giúp: lần 1 đúng 30,0%, lần 3 chỉ 2,2%) và `doi_tac` (0,85×, có điều khoản riêng) khỏi phạm vi (`simulated`). Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2026-12-04.
- Giám đốc vận hành ký chấp nhận mức chênh 6 điểm (power 0,64 nếu chênh thật chỉ 5 điểm). Phụ trách: Giám đốc vận hành. Kiểm tra: 2026-12-04.
- Thay hai cột phút `simulated` bằng phút đo thật từ event `nhan_vien_xem_lai`, `nhan_vien_lam_lai_xong`. Phụ trách: PM trợ lý hoàn phí. Kiểm tra: 2026-12-11, cuối tuần 1.
- Có lộ trình giảm xem lại theo bậc, vì xem lại 100% làm chi phí lên 0,98–1,04× (`simulated`). Phụ trách: Trưởng nhóm CSKH. Kiểm tra: 2026-12-18, cuối bước 0.25.
