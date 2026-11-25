# Team

## Thông tin nhóm

- Tên nhóm: Dota
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Dota-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/phungtr/K5-L3B-DAY13-Dota-LaunchEconomics · `main` · commit chốt nội dung `e789167` (commit sau đó chỉ cập nhật `TEAM.md`)

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

- Chốt phân vai và lịch theo checkpoint; nhóm làm theo nhánh riêng và pull request.
- CP3: gắn nhãn độc lập 20 ca, đồng thuận với người gắn nhãn 1 là 16/20 = 80%.
- Giữ hồ sơ `ho_so_launch_v0.md`: điền dần mục 1–7 theo từng CP, chốt đề xuất Go có điều kiện với 5 điều kiện có người phụ trách và ngày kiểm tra.
- CP4: sửa phạm vi pilot từ 6 depot thành cả 12 depot (chia 20 + 20 cần 40 nhân viên), tính lại ngày quyết định 2027-01-08.
- Viết `group_report.md`; review và merge PR #3, #4, #7, #10.
- Duyệt chéo: chuẩn bị bài trình và câu trả lời cho 5 câu hỏi của hội đồng Bá Khí; chấm nhóm Bá Khí trong `phieu_cham.md` (30/30, Go có điều kiện).
- Sau duyệt chéo: sửa luật dừng trong `pilot_plan.yaml` theo slide chữa D3/A4, thêm event sổ cái và dòng rủi ro tiền thuê, cập nhật hồ sơ.

### Bằng chứng

- Commit `8f84bd5` (`TEAM.md`), `edd41d4` (hồ sơ mục 1–3, `group_report.md`), `f1dea60` (`report/team/cp3_nhan_doc_lap_nguoi_2.md`), `06ba839` (`pilot_plan.yaml`, hồ sơ mục 5–6), `83d9b8e` (báo cáo cá nhân), `969b39a` (hồ sơ mục 4, 7 và đề xuất), `14766c4` (`phieu_cham.md`), `c0c568b` (sửa sau duyệt chéo).
- Báo cáo cá nhân: `report/team/2A202604094_PhungQuangTra.md`.

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

- Cài môi trường `src/.venv` (Python 3.12.16) trên Linux; đối chiếu độc lập dữ liệu CSV với output của Tuấn và hoàn thiện bảng A1–A4, B1–B4 trong `report/team/bang_chi_phi.md` (gắn nhãn `simulated`, kiểm quy luật đối xứng B1 và độ nhạy B4 ở mức 9 phút `11.743 đ = 0,98×` vs TB dữ liệu `15,3`–`16,25` phút).
- Viết code CP4 (`co_mau()`, `tinh_d1()` tính 5 câu D1, `DE = 6,96`, `m ≥ 299`, power 5 điểm `0,64`, tỉ lệ `mo_lai_trong_7_ngay` `4,25%`/`3,97%`) và CP5 (`tinh_e1()` tính 3 chỉ số E1) trong `src/lab13.py`; điền 3 kết quả tính thử E1 (`82,83%`, `27,12%`, `4,25%`) vào `report/team/chi_so.md`.
- Bổ sung `ti_le_ok_theo_lan_chay()` (`quoc_te`: `30,0% → 11,4% → 2,2%`) và tham số `phut_lam_lai=9` cho `xem_lai_tat_ca()` trong `src/lab13.py` để khớp toàn bộ số trích dẫn trong hồ sơ.
- *(Chờ bổ sung sau 17:00: đối chiếu `pilot_plan.yaml` nhóm được chấm khi duyệt chéo Gate 2a.)*

### Bằng chứng

- Commit `df1ca8b` (PR #2, merge `90aa388`): `report/team/bang_chi_phi.md` (A1–A4, B1–B4).
- Commit `3c81b92` (PR #5, merge `5fa74d0`): `src/lab13.py` (D1 cỡ mẫu và tỉ lệ mở lại 7 ngày).
- Commit `c992b8e` (PR #8, merge `5ea4d1b`): `src/lab13.py` (`tinh_e1()`) và `report/team/chi_so.md` (3 chỉ số tính thử E1).
- Commit `b6cd818` (PR #11, merge `f14fd93`): `src/lab13.py` (A3 tỉ lệ `ok` theo lần chạy và B4 giả định 9 phút làm lại).
- Báo cáo cá nhân: `report/team/2A202604019_LaiTrongDuc.md`.

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
- Chạy kiểm chứng độc lập bản `src/lab13.py` mới nhất (commit `b2ee9b2`, Python 3.13.5 với `src/requirements.txt`): ba phép thử A1 `ĐẠT`, khớp toàn bộ A2–E1 (gồm A3 theo `attempt` và B4 3 mốc), `yaml.safe_load` trên `pilot_plan.yaml` đạt, soát `0` từ bị cấm và `0` dấu `?`.
- *(Chờ bổ sung sau 17:00: điền kết quả chấm nhóm bạn trong `report/team/phieu_cham.md` khi duyệt chéo Gate 2a.)*

### Bằng chứng

- Commit `7ac1a45` (`report/team/chi_so.md`, `report/team/2A202604013_NguyenBaoTrung.md`).
- Commit `7116fae` (`report/team/bang_loi.md`: 16/20 đồng thuận, 4 quy tắc, 5 ca khắc phục).
- Commit `c552549` (`report/team/chi_so.md` nhãn `simulated` bảng E2, `TEAM.md`, báo cáo cá nhân).
- Commit `0fd8ab1` (`report/team/phieu_cham.md` prefill nhóm hội đồng `Dota (L3B)`, tự đánh giá cá nhân).
- Kết quả chạy độc lập `src/lab13.py` tại commit `b2ee9b2` (A1 `ĐẠT`, A2 `4.472 đ` [`simulated`], E1 `82,83%` / `27,12%` / `4,25%`, `pilot_plan.yaml` hợp lệ).
- `report/team/2A202604013_NguyenBaoTrung.md` (báo cáo cá nhân).
