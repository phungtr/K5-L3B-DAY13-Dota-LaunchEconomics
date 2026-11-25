# Báo cáo cá nhân — LaiTrongDuc-2A202604019

## 1. Thông tin thành viên

- Họ tên: Lại Trọng Đức
- MSSV: 2A202604019
- Email: laitrongducc@gmail.com
- Vai trong nhóm: Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5)

## 2. Phần việc phụ trách

- Cài môi trường Python `venv` và thư viện cần thiết trên máy 2 (`src/.venv`).
- Người kiểm số (CP1–CP2): tính tay một con số để đối chiếu với kết quả của Tuấn; điền A1–A4 và B1–B4 vào `report/team/bang_chi_phi.md`; kiểm tra quy luật tự đối chiếu ở B1–B4.
- Người viết code (CP4–CP5): viết code phần D1 (a–e), tỉ lệ `mo_lai_trong_7_ngay` và tính thử 3 chỉ số E1 trong `src/lab13.py`.
- Giữ và hoàn thiện file `report/team/pilot_plan.yaml` (ghép D2 và ba luật dừng, kiểm tra `yaml.safe_load` và không còn dấu `?`).
- Điền bảng đặc tả chỉ số E1 vào `report/team/chi_so.md`.
- Duyệt chéo Gate 2a: đối chiếu `pilot_plan.yaml` trong hồ sơ của nhóm được chấm.

## 3. Đóng góp cụ thể

- **Cài đặt môi trường & quy trình Git:** Tạo `src/.venv` với Python 3.12.16 trên Linux và cài đủ thư viện (`pandas`, `numpy`, `scipy`, `statsmodels`, `pyyaml`); luôn làm việc theo từng nhánh riêng và mở Pull Request vào `main` để tránh xung đột với các thành viên khác.
- **CP1–CP2 (Người kiểm số):** Đối chiếu độc lập kết quả `src/lab13.py` của Tuấn trực tiếp với hai file `src/logix_runs.csv` và `src/logix_requests.csv`, rồi hoàn thiện toàn bộ bảng A1–A4 và B1–B4 trong `report/team/bang_chi_phi.md` (A1 đạt `1,20 · 1,25 · 1,25`; A2 `4.472 đ/việc` `simulated`, gấp `16,3` lần hoá đơn `274,7 đ/yc`, chi phí cả hệ thống `5.865 đ = 0,49×` `simulated`; A3 xác định loại `quoc_te` `22.515 đ = 1,88×` và `doi_tac` `0,85×` không đưa vào pilot; A4 cộng cố định 40 triệu/tháng ra `4.599 đ = 0,38×` ở `45.000` yc/tháng và `5.784 đ = 0,48×` khi giảm nửa khối lượng; kiểm quy luật đối xứng B1 và ghi rõ độ nhạy B4 giữa giả định 9 phút làm lại `11.743 đ = 0,98×`, TB toàn mẫu `15,3` phút `12.414 đ = 1,03×`, và dữ liệu trực tiếp `12.516 đ = 1,04×`, đều gắn nhãn `simulated`).
- **CP4 (Người viết code):** Bổ sung `co_mau()` và `tinh_d1()` trong `src/lab13.py` để tính đủ 5 câu D1 (`1.251`, `3.103` với `DE=2,48` cần 84 người > 40, tối đa `1.000` ở 20 nhân viên/nhóm, tối đa `300` ở 6 depot/nhóm, mức chênh 6 điểm `859/nhóm` cần `m ≥ 299`, `DE=6,96`, power ở mức chênh 5 điểm = `0,64` bằng `statsmodels.NormalIndPower`) và tỉ lệ `mo_lai_trong_7_ngay` hiện tại (`4,25%` toàn mẫu; `3,97%` phạm vi `noi_dia + hang_nang`).
- **CP5 · E1 (Người viết code):** Bổ sung `tinh_e1()` trong `src/lab13.py` và điền 3 ô tính thử E1 vào `report/team/chi_so.md` (`82,83%` đóng trong 24h và không mở lại 7 ngày, `27,12%` bỏ qua gợi ý `sua`/`bo`, `4,25%` mở lại trong 7 ngày), giữ đúng nguyên tắc không dùng nhóm đối chứng giả.
- **Hoàn thiện bổ sung A3 & B4 trong `src/lab13.py`:** Thêm `ti_le_ok_theo_lan_chay()` (`quoc_te` tụt `30,0% → 11,4% → 2,2%`) và mở rộng `xem_lai_tat_ca()` hỗ trợ tham số `phut_lam_lai=9` (`11.743 đ = 0,98×`) cùng mức TB toàn mẫu `15,3` phút để mã nguồn in đủ các số đang trích dẫn trong hồ sơ.
- *(Chờ bổ sung sau 17:00: đối chiếu `pilot_plan.yaml` của nhóm bạn trong phần duyệt chéo Gate 2a.)*

## 4. Bằng chứng

- Commit `df1ca8b` (PR #2, merge `90aa388`): `report/team/bang_chi_phi.md` (đầy đủ A1–A4, B1–B4, nhãn `simulated`, đối xứng B1).
- Commit `3c81b92` (PR #5, merge `5fa74d0`): `src/lab13.py` (`co_mau()`, `tinh_d1()` tính 5 câu D1 và tỉ lệ `mo_lai_trong_7_ngay`).
- Commit `c992b8e` (PR #8, merge `5ea4d1b`): `src/lab13.py` (`tinh_e1()`) và `report/team/chi_so.md` (3 chỉ số tính thử E1).
- Commit `b6cd818` (PR #11, merge `f14fd93`): `src/lab13.py` (`ti_le_ok_theo_lan_chay()` ra `30,0% → 11,4% → 2,2%` cho `quoc_te`; `xem_lai_tat_ca()` với giả định 9 phút làm lại ra `11.743 đ = 0,98×`).
- Cập nhật `TEAM.md` phần đóng góp và bằng chứng của `LaiTrongDuc-2A202604019`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (Gemini) trong IDE.
- **Dùng vào việc:** Đọc nhanh đề bài và phân vai trong repo; hướng dẫn cài đặt môi trường Python `venv` trên Linux; gợi ý code cho hàm `co_mau()`, `tinh_d1()`, `tinh_e1()`, `ti_le_ok_theo_lan_chay()`, và tham số hoá `xem_lai_tat_ca()` trong `src/lab13.py`; hỗ trợ tính đối chiếu độc lập từ hai file CSV, trình bày bảng `report/team/bang_chi_phi.md`, `report/team/chi_so.md` và soạn báo cáo cá nhân này.
- **Không dùng AI:** Không dùng AI để tự bịa số liệu hay thay thế phần chạy code thực tế; mọi con số trong báo cáo đều lấy từ output chạy `src/lab13.py` hoặc script đối chiếu trực tiếp trên `logix_runs.csv` và `logix_requests.csv`.
- **Cách tự kiểm tra kết quả:**
  - Chạy lại `.venv/bin/python lab13.py` trong `src/` sau mọi lần sửa để kiểm tra 3 phép thử A1 in `ĐẠT` (`1,20 · 1,25 · 1,25`) và từng con số A2–A4, B1–B4, D1, E1 khớp với bảng đối chiếu.
  - Kiểm tra tính chất tự đối chiếu ở B1 (kịch bản giảm một nửa giảm đúng bằng nửa mức tăng của kịch bản gấp đôi) và kiểm tra `yaml.safe_load`, không còn dấu `?`, không còn từ bị cấm trong `report/team/`.
  - Tự nắm vững cách giải thích cho hội đồng: lý do tử số tính mọi lần chạy còn mẫu số chỉ tính việc thành công, công thức cỡ mẫu hiệu dụng `c × m / DE < c / ICC` khi chia theo cụm, và sự khác biệt giữa tối ưu chi phí mỗi việc thành công (1 lần) với tối ưu chi phí cả hệ thống (2 lần).

## 6. Tự đánh giá

- **Làm được:** Chủ động cài môi trường và kiểm tra số liệu độc lập trực tiếp từ CSV trước khi điền `bang_chi_phi.md`; giữ kỷ luật tạo nhánh riêng và PR cho từng checkpoint nên không gây xung đột code/hồ sơ với nhóm; hoàn thiện đầy đủ code D1, E1 và bổ sung kịp phần A3 `ok` theo lần chạy và B4 mức 9 phút vào `src/lab13.py`.
- **Chưa tốt:** Có lúc làm trước sang CP5 khi đang ở nhịp CP4 nên phải tách nhánh lại để giữ đúng thứ tự checkpoint và phân vai; ở lượt code CP1–CP2 ban đầu chưa bổ sung ngay phần tính tỉ lệ `ok` theo lần thử và B4 9 phút vào `src/lab13.py` cho tới khi rà lại hồ sơ.
- **Lần sau:** Bám sát đúng thứ tự từng checkpoint trước khi chuyển bước kế tiếp, và đối chiếu danh sách mọi con số xuất hiện trong hồ sơ với output của script chính ngay từ đầu.
