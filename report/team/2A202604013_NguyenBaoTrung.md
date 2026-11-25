# Báo cáo cá nhân — NguyenBaoTrung-2A202604013

## 1. Thông tin thành viên

- Họ tên: Nguyễn Bảo Trung
- MSSV: 2A202604013
- Email: nbtrungrhm@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề, theo dõi điều kiện "Xong khi" của từng CP.
- Gắn nhãn độc lập 20 ca lỗi; viết `report/team/bang_loi.md`.
- Danh sách event và hai chỉ số tự đề xuất trong `report/team/chi_so.md`.
- Viết `report/team/phieu_cham.md` khi nhóm làm hội đồng; chạy thử `lab13.py` trên máy khác trước khi nộp.

## 3. Đóng góp cụ thể

- **Soát "Xong khi" CP1–CP2:** Chạy kiểm tra độc lập `src/lab13.py` trên máy cá nhân (xác nhận ba phép thử A1 ĐẠT, chi phí mỗi việc thành công `4.472 đ` [simulated] gấp 16,3 lần hoá đơn `275 đ`/yêu cầu, phép thử giảm nửa = nửa mức tăng và cộng tuyến tính B2 khớp) và rà soát `report/team/bang_chi_phi.md` (nhãn `simulated`, không có từ bị cấm).
- **CP3 (`report/team/bang_loi.md`):** Tự gắn nhãn độc lập toàn bộ 20 ca lỗi theo 5 loại Google PAIR trước khi xem nhãn của Trà (`cp3_nhan_doc_lap_nguoi_2.md`); so nhãn đạt đồng thuận `16/20 = 80%` (đạt ngưỡng ≥ 80%); cùng Trà thống nhất nhãn và viết 4 câu quy tắc phân biệt cho 4 ca không trùng (Ca 1, 3, 8, 13); thiết kế bảng khắc phục cho 5 ca đủ 5 loại (Ca 14, 7, 16, 4, 5) gắn trực tiếp với danh sách event đo được và vai trò phụ trách cụ thể.
- **CP4 (`report/team/pilot_plan.yaml`):** Chạy kiểm tra độc lập code D1 trong `src/lab13.py` (commit `5fa74d0`, khớp 5 câu D1 và tỉ lệ mở lại 7 ngày `4,25%` toàn mẫu / `3,97%` phạm vi) và soát điều kiện "Xong khi" trên `pilot_plan.yaml` (commit `d458ec8`: YAML hợp lệ, `0` dấu `?`, `0` từ bị cấm, đủ 20 cụm/nhóm với đánh đổi MDE 6 điểm và đủ 3 luật dừng).
- **CP5 (`report/team/chi_so.md` & soát "Xong khi"):** Thiết kế 2 chỉ số tự đề xuất (chỉ số Dùng theo độ phủ nhân viên k/n mỗi tuần dựa trên số liệu thật 20 nhân viên ở 6 depot; chỉ số An toàn về tỉ lệ gợi ý được giữ nguyên nhưng vẫn mở lại trong 7 ngày), thiết kế 9 event có `trace_id` (gồm cả event `kiem_tra_mau_hoan_tien` bắt lỗi ngầm) và lập phần kiểm tra chéo chỉ số → event. Sau khi Đức (PR #8) và Tuấn (PR #9) hoàn thành E1–E2, đối chiếu độc lập 3 chỉ số E1 trên `logix_requests.csv` (`82,83%` = `994/1.200`, `27,12%` = `48/177`, `4,25%` = `51/1.200`), bổ sung nhãn `simulated` còn thiếu ở bảng E2 (`chi_so.md`), và soát quy tắc bắt buộc toàn `report/team/` (`0` từ bị cấm, `0` dấu `?` trong `pilot_plan.yaml`, `0` vi phạm người phụ trách).
- *(Đang chờ hoàn thiện ở phần sau của buổi lab: viết `report/team/phieu_cham.md` khi duyệt chéo Gate 2a lúc 17:00 và chạy kiểm tra cuối `src/lab13.py` bằng `.venv` lúc 17:45.)*

## 4. Bằng chứng

- Commit `7ac1a45` (`chi_so: event list, 2 proposed metrics, cross-check (Trung)`): `report/team/chi_so.md` (2 chỉ số tự đề xuất, 9 event có `trace_id`, mục kiểm tra chéo) và khởi tạo `report/team/2A202604013_NguyenBaoTrung.md`.
- Commit `7116fae` (`docs(cp3): complete bang_loi.md with 16/20 agreement and 5-case remediation (Trung)`): `report/team/bang_loi.md` (hai bộ nhãn độc lập giữ nguyên gốc, đồng thuận `16/20 = 80%`, 4 quy tắc phân biệt Ca 1/3/8/13, bảng khắc phục 5 ca: 14, 7, 16, 4, 5).
- Kết quả chạy kiểm tra `src/lab13.py` trên máy cá nhân (từ commit `0bd3f2d`): ba phép thử A1 ĐẠT, `cps = 4.472 đ` (`simulated`), 978 việc thành công; đối chiếu độc lập 3 chỉ số E1 và toàn bộ bảng A1–E1 từ commit `a7f9391` trên `logix_runs.csv` và `logix_requests.csv`.
- *(Sẽ bổ sung commit của `phieu_cham.md` và kết quả chạy cuối `src/lab13.py` bằng `.venv` sau 17:00.)*

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI Antigravity (IDE/CLI).
- **Mục đích sử dụng:**
  - Soạn nháp danh sách 9 event, 2 chỉ số tự đề xuất và kiểm tra chéo cho `report/team/chi_so.md`.
  - Trích xuất định nghĩa 5 loại lỗi Google PAIR và 20 ca lỗi từ đề bài để bản thân tự đọc và gắn nhãn từng ca; chạy script Python đối chiếu bộ nhãn độc lập với Trà để tính tỉ lệ đồng thuận (`16/20 = 80%`) và định dạng bảng vào `report/team/bang_loi.md`.
  - Gợi ý cấu trúc bảng khắc phục 5 ca và soát lỗi định dạng (kiểm tra không sót `...`, không chứa từ bị cấm).
- **Cách tự kiểm tra:**
  - Tự duyệt từng mục của `chi_so.md` (so sánh ưu/nhược giữa chỉ số theo nhân viên và theo yêu cầu trên số liệu đếm thật 20 nhân viên / 177 ca xem lại từ `logix_requests.csv`, tự quyết định thêm event 9 bắt lỗi ngầm).
  - Tự gắn nhãn độc lập toàn bộ 20 ca lỗi không để AI gắn thay và không xem đáp án hay nhãn của Trà trước; trao đổi và thống nhất trực tiếp với Trà cho 4 ca không trùng (1, 3, 8, 13); duyệt từng dòng trong bảng khắc phục 5 ca trước khi ghi vào file.
  - Mọi số đếm (20 nhân viên, 177 ca xem lại, 16/20 = 80% đồng thuận, kết quả `src/lab13.py`) đều được kiểm chứng bằng mã Python chạy trực tiếp trên dữ liệu.

## 6. Tự đánh giá

*(Chưa chốt — sẽ điền sau khi hoàn thành soát CP4, duyệt chéo Gate 2a lúc 17:00 và chạy kiểm tra cuối `src/lab13.py`.)*
