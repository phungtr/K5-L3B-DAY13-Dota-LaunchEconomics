# Team

## Thông tin nhóm

- Tên nhóm: Dota
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Dota-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/phungtr/K5-L3B-DAY13-Dota-LaunchEconomics · `main` · (điền hash commit chốt khi nộp)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phùng Quang Trà | 2A202604094 | traquangphung@gmail.com | phungtr | Nhóm trưởng · Người gắn nhãn 2, kiêm giữ hồ sơ |
|   2 | Trần Văn Tuấn | 2A202604092 | quyvangia2004@gmail.com | tuanq0 | Người viết code (CP1–CP2) → Người kiểm số (CP4–CP5) |
|   3 | Lại Trọng Đức | 2A202604019 | laitrongducc@gmail.com | laitrongduc | Người kiểm số (CP1–CP2) → Người viết code (CP4–CP5) |
|   4 | Nguyễn Bảo Trung | 2A202604013 | nbtrungrhm@gmail.com | trungnb | Người gắn nhãn 1 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí: Tuấn viết code CP1–CP2, Đức viết code CP4–CP5.

## Phân công theo checkpoint

| Giờ | Trà (giữ hồ sơ, gắn nhãn 2) | Tuấn | Đức | Trung (gắn nhãn 1) |
| --- | --- | --- | --- | --- |
| 14:00 Chuẩn bị | Mời 3 bạn làm collaborator repo; mở `ho_so_launch_v0.md` | Cài venv máy 1, chạy `lab13.py` | Cài venv máy 2 | Đọc đề, ghi điều kiện "Xong khi" của từng CP |
| 14:10 CP1 · A | Điền dần mục 1, 3 của hồ sơ | **Code:** A1 (ba phép thử ĐẠT), `mo_hinh`, A3, A4 | **Kiểm số:** tính tay một con số để đối chiếu; điền A1–A4 vào `bang_chi_phi.md` | Soát "Xong khi" CP1, nhãn `simulated` |
| 14:53 CP2 · B | Điền mục 2 của hồ sơ | **Code:** B1 (9 kịch bản), B2, B3, B4 | Điền B1–B4 vào `bang_chi_phi.md`; kiểm "giảm nửa = nửa mức tăng" | Soát mỗi câu ≤ 3 dòng, có số |
| 15:20 Giải lao | | Push `lab13.py` | Pull `lab13.py` để nhận code | |
| 15:35 CP3 · C | Gắn nhãn 20 ca độc lập (8 phút), rồi so nhãn với Trung | Hoàn thiện B nếu còn | Hoàn thiện B nếu còn | Gắn nhãn 20 ca độc lập; **viết `bang_loi.md`** (đồng thuận, quy tắc, bảng khắc phục 5 ca) |
| 16:08 CP4 · D | Điền mục 5, 6 của hồ sơ | **Kiểm số:** tính tay D1 câu b, e; viết D2 và ba luật dừng | **Code:** D1 a–e, tỉ lệ `mo_lai_trong_7_ngay`; **giữ file `pilot_plan.yaml`** | Soát: không còn `?`, đủ 20 cụm mỗi nhóm hoặc có ghi đánh đổi |
| 16:36 CP5 · E | **Chốt `ho_so_launch_v0.md`:** 7 mục + đề xuất | E2: ít nhất 2 dòng rủi ro kinh tế (số lấy từ B) | Code + điền 3 chỉ số E1 | Ít nhất 6 event có `trace_id`, 2 chỉ số tự đề xuất, kiểm tra chéo |
| 17:00 Duyệt chéo | Gửi hồ sơ, trình 1 phút, trả lời câu hỏi | Đối chiếu số trong hồ sơ nhóm được chấm | Đối chiếu pilot plan nhóm được chấm | **Viết `phieu_cham.md`** |
| 17:45 Nộp | `group_report.md`, chạy checklist, push cuối | Báo cáo cá nhân | Báo cáo cá nhân | Chạy `lab13.py` trên máy khác; báo cáo cá nhân |

Mỗi file chỉ một người sửa (`pilot_plan.yaml` sửa trên máy Đức) để tránh xung đột khi push. Luôn `git pull` trước khi `git push`.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Tên file của nhóm:

- `report/team/2A202604094_PhungQuangTra.md`
- `report/team/2A202604092_TranVanTuan.md`
- `report/team/2A202604019_LaiTrongDuc.md`
- `report/team/2A202604013_NguyenBaoTrung.md`

## PhungQuangTra-2A202604094

### Phần việc phụ trách

- Nhóm trưởng: quản lý repo, mời collaborator, push bản cuối, chạy checklist nộp bài.
- Người gắn nhãn 2: gắn nhãn độc lập 20 ca lỗi ở CP3, so nhãn cùng Trung.
- Giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi, chốt đề xuất; viết `report/team/group_report.md`.
- Trình hồ sơ trước hội đồng Gate 2a.

### Đóng góp cụ thể

- (điền sau buổi lab)

### Bằng chứng

- (commit, file, con số)

## TranVanTuan-2A202604092

### Phần việc phụ trách

- Người viết code CP1–CP2: `src/lab13.py` phần A1, `mo_hinh`, A3, A4, B1–B4.
- Người kiểm số CP4–CP5: tính tay D1 câu b và e; viết D2 và ba luật dừng trong `pilot_plan.yaml`.
- E2: các dòng rủi ro kinh tế trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- Viết `src/lab13.py` cho CP1–CP2: ba hàm A1 (ba phép thử ĐẠT: 1,20 · 1,25 · 1,25), `mo_hinh`, bảng A3 theo loại, bảng A4 chi phí cố định, và B1–B4 (bảng độ nhạy, cặp yếu tố, giới hạn chạy, xem lại 100%).
- Kiểm số D1 câu b (3.103 mỗi nhóm, cần 84 người > 40) và câu e (m ≥ 299, 859 mỗi nhóm); viết D2 năm câu và ba luật dừng trong `report/team/pilot_plan.yaml`.
- Viết ba dòng rủi ro kinh tế E2 trong `report/team/chi_so.md`, số lấy từ B1 và B4.

### Bằng chứng

- Commit `20705cb`: `src/lab13.py` (CP1–CP2). Chạy `PYTHONUTF8=1 python lab13.py` in ĐẠT và A2: chi phí mỗi việc thành công 4.472 đ (simulated), 978 việc thành công.
- Commit `dcdc852`: `report/team/pilot_plan.yaml` (D2, ba luật dừng, cỡ mẫu 859, design effect 6,96).
- Commit `1110294`: `report/team/chi_so.md` (E2, ba dòng rủi ro).
- Báo cáo cá nhân: `report/team/2A202604092_TranVanTuan.md`.

## LaiTrongDuc-2A202604019

### Phần việc phụ trách

- Người kiểm số CP1–CP2: tính tay đối chiếu, điền `report/team/bang_chi_phi.md`.
- Người viết code CP4–CP5: `src/lab13.py` phần D1 và ba chỉ số E1; giữ file `report/team/pilot_plan.yaml`.
- E1: bảng đặc tả chỉ số trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- (điền sau buổi lab)

### Bằng chứng

- (commit, file, con số)

## NguyenBaoTrung-2A202604013

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" của từng CP.
- Gắn nhãn độc lập 20 ca lỗi; viết `report/team/bang_loi.md`.
- Danh sách event và hai chỉ số tự đề xuất trong `report/team/chi_so.md`.
- Viết `report/team/phieu_cham.md` khi nhóm làm hội đồng; chạy thử `lab13.py` trên máy khác trước khi nộp.

### Đóng góp cụ thể

- Soát điều kiện "Xong khi", nhãn `simulated` và quy tắc bắt buộc qua các CP1–CP5 (`bang_chi_phi.md`, `pilot_plan.yaml`, `chi_so.md`); đối chiếu độc lập kết quả `src/lab13.py` (A1–E1).
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, so nhãn với Trà đạt đồng thuận `16/20 = 80%`, viết 4 quy tắc phân biệt (Ca 1, 3, 8, 13) và bảng khắc phục 5 ca (Ca 14, 7, 16, 4, 5) trong `report/team/bang_loi.md`.
- Thiết kế 2 chỉ số tự đề xuất, 9 event có `trace_id` (gồm event `kiem_tra_mau_hoan_tien` bắt lỗi ngầm) và phần kiểm tra chéo chỉ số → event trong `report/team/chi_so.md`.
- *(Chờ bổ sung sau 17:00: viết `report/team/phieu_cham.md` khi duyệt chéo Gate 2a và chạy kiểm cuối `src/lab13.py`.)*

### Bằng chứng

- Commit `7ac1a45` (`report/team/chi_so.md`, `report/team/2A202604013_NguyenBaoTrung.md`).
- Commit `7116fae` (`report/team/bang_loi.md`: 16/20 đồng thuận, 4 quy tắc, 5 ca khắc phục).
- `report/team/2A202604013_NguyenBaoTrung.md` (báo cáo cá nhân).
