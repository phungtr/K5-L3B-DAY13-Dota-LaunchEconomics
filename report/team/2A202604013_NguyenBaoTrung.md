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
- **Kiểm tra độc lập `src/lab13.py` và checklist nộp bài (commit `b2ee9b2`, đã gồm PR #11 và PR #12):** Chạy hoàn chỉnh `src/lab13.py` trên máy cá nhân (macOS, Python 3.13.5, cài đúng `src/requirements.txt` gồm `pandas 3.1.1`, `scipy 1.18.1`, `statsmodels 0.15.0`, `pyyaml 6.0.4` trong venv sạch ngoài iCloud vì `src/.venv` trên Desktop bị iCloud đẩy thành `dataless`): `exit code 0`, ba phép thử A1 in `ĐẠT`, toàn bộ A2–E1 (kể cả tỉ lệ `ok` theo `attempt` ở A3 và 3 mốc B4) khớp hồ sơ (ghi nhận lệch làm tròn `1 đ` ở mốc B4 trung bình toàn mẫu: code in `12.415 đ` so với `12.414 đ` trong bảng, cùng tỉ số `1,03×`); xác nhận `yaml.safe_load` trên `pilot_plan.yaml` đạt, `0` từ bị cấm, `0` dấu `?` ngoài chú thích, `0` vi phạm người phụ trách.
- *(Còn 1 đầu việc cuối ở phần duyệt chéo 17:00: điền kết quả chấm nhóm bạn vào `report/team/phieu_cham.md` — đã điền sẵn tên nhóm hội đồng `Dota (L3B)` ở commit `0fd8ab1`.)*

## 4. Bằng chứng

- Commit `7ac1a45` (`chi_so: event list, 2 proposed metrics, cross-check (Trung)`): `report/team/chi_so.md` (2 chỉ số tự đề xuất, 9 event có `trace_id`, mục kiểm tra chéo) và khởi tạo `report/team/2A202604013_NguyenBaoTrung.md`.
- Commit `7116fae` (`docs(cp3): complete bang_loi.md with 16/20 agreement and 5-case remediation (Trung)`): `report/team/bang_loi.md` (hai bộ nhãn độc lập giữ nguyên gốc, đồng thuận `16/20 = 80%`, 4 quy tắc phân biệt Ca 1/3/8/13, bảng khắc phục 5 ca: 14, 7, 16, 4, 5).
- Commit `c552549` (`docs(cp5): update Trung report, TEAM.md section, and simulated label in chi_so.md`): bổ sung nhãn `simulated` bảng E2 trong `report/team/chi_so.md`, điền phần đóng góp trong `TEAM.md` và cập nhật báo cáo cá nhân.
- Commit `0fd8ab1` (`docs: complete Trung self-assessment and prefill council team in phieu_cham.md`): hoàn thiện mục tự đánh giá và điền sẵn thông tin nhóm hội đồng `Dota (L3B)` trong `report/team/phieu_cham.md`.
- Chạy kiểm chứng `src/lab13.py` trên máy cá nhân tại commit `b2ee9b2` (Python 3.13.5, `src/requirements.txt`): ba phép thử A1 `ĐẠT`, A2 `4.472 đ` (`simulated`, 978 việc thành công), A3 theo `attempt` (`quoc_te`: `30,0% → 11,4% → 2,2%`), A4 (`4.599 đ` / `5.784 đ`, `simulated`), B1–B3, B4 3 mốc (`11.743 đ` / `12.415 đ` / `12.516 đ`, `simulated`), D1 (`1.251`, `m >= 299`, `power = 0,64`), E1 (`82,83%`, `27,12%`, `4,25%`), và `yaml.safe_load` trên `pilot_plan.yaml` đạt.
- *(Sẽ bổ sung commit hoàn thiện `report/team/phieu_cham.md` sau phần duyệt chéo Gate 2a lúc 17:00.)*

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

- **Điểm làm tốt:**
  - Giữ đúng tính độc lập khi gắn nhãn CP3 (tự gắn đủ 20 ca trước khi so với Trà, đạt đồng thuận `16/20 = 80%`), chốt 4 quy tắc phân biệt rõ cho 4 ca lệch và gắn bảng khắc phục 5 ca trực tiếp với event đo được cùng vai trò phụ trách cụ thể.
  - Thiết kế hệ thống 9 event có `trace_id` (gồm cả event `kiem_tra_mau_hoan_tien` bắt lỗi ngầm) và lập kiểm tra chéo bao phủ toàn bộ chỉ số E1 lẫn chi phí đo thật trong pilot.
  - Soát đều điều kiện "Xong khi" qua các CP1–CP5 (phát hiện và bổ sung nhãn `simulated` còn thiếu ở bảng E2 trong `chi_so.md`, đối chiếu độc lập các con số của `src/lab13.py`, đảm bảo `0` từ bị cấm và `0` dấu `?` trong `pilot_plan.yaml`).
- **Điểm cần rút kinh nghiệm & việc còn lại:**
  - Ở CP3 còn lệch 4 ca (`Ca 1, 3, 8, 13`) do lúc đầu nghiêng về "chỗ hệ thống cần sửa" thay vì nguyên nhân gốc; sau khi thảo luận đã nắm rõ hơn cách phân biệt giữa lỗi do người dùng, ngữ cảnh, giới hạn hệ thống và lỗi hệ thống.
  - Còn 1 đầu việc cuối buổi theo phân công: điền kết quả chấm nhóm bạn vào `report/team/phieu_cham.md` khi duyệt chéo Gate 2a lúc 17:00.
