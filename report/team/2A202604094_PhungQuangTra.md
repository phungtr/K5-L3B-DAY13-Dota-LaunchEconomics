# Báo cáo cá nhân — PhungQuangTra-2A202604094

## 1. Thông tin thành viên

- Họ tên: Phùng Quang Trà
- MSSV: 2A202604094
- Email: traquangphung@gmail.com
- Vai trong nhóm: Nhóm trưởng · Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Nhóm trưởng: quản lý repo nhóm, phân vai, chạy checklist nộp bài, push bản cuối.
- Người gắn nhãn 2: gắn nhãn độc lập 20 ca lỗi ở CP3, so nhãn cùng người gắn nhãn 1.
- Giữ hồ sơ: điền `report/team/ho_so_launch_v0.md` từ đầu buổi, chốt đề xuất; viết `report/team/group_report.md`.
- Trình hồ sơ trước hội đồng Gate 2a.

## 3. Đóng góp cụ thể

- **Tổ chức nhóm:** chốt phân vai bốn người và lịch theo checkpoint trong `TEAM.md`; nhóm làm theo nhánh riêng và pull request nên không bị xung đột file, đi sớm lịch khoảng 40 phút ở CP4.
- **Cài đặt:** tự cài môi trường Python trên máy Windows; xử lý lỗi `python3`/`source` không chạy trong PowerShell bằng lệnh Windows (ghi ở mục 5 của `group_report.md`).
- **CP3 · gắn nhãn 2:** tự gắn nhãn độc lập 20 ca trong 8 phút, không trao đổi, không xem nhãn tham khảo; đưa bộ nhãn gốc lên `report/team/cp3_nhan_doc_lap_nguoi_2.md` để so với người gắn nhãn 1. Đồng thuận 16/20 = 80%.
- **Giữ hồ sơ:** điền `ho_so_launch_v0.md` dần theo từng CP: mục 1–3 sau CP1–CP2 (4.472 đ/việc thành công, 5.865 đ/yêu cầu = 0,49×, đều `simulated`), mục 5 sau CP3, mục 6 sau CP4; viết bản nháp đề xuất Go có điều kiện với 5 điều kiện, mỗi điều kiện có người phụ trách và ngày kiểm tra.
- **CP4 · rà soát pilot:** phát hiện phạm vi "6 depot chạy thử" mâu thuẫn với cách chia 20 + 20 nhân viên (đợt chạy thử chỉ có 6 depot, 20 nhân viên, nên chỉ chia được 10 + 10, dưới 20 cụm); sửa thành cả 12 depot. Tính lại ngày quyết định: 30,7 yêu cầu/người/ngày → khoảng 10 ngày để đủ 299 yêu cầu mỗi người, cộng 7 ngày theo dõi mở lại → 2027-01-08.
- **Quản lý repo:** review và merge PR #3, #4, #7; dựng `group_report.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `8f84bd5` "team md": phân vai và lịch trong `TEAM.md`.
- `edd41d4`: hồ sơ mục 1–3, `group_report.md`, báo cáo cá nhân này.
- `f1dea60`: bộ nhãn độc lập của người gắn nhãn 2, `report/team/cp3_nhan_doc_lap_nguoi_2.md`.
- `06ba839`: `pilot_plan.yaml` sửa phạm vi 12 depot và `decision_date` 2027-01-08; hồ sơ mục 5–6.
- Merge PR #3 (`e810e49`), #4 (`a3bc063`), #7 (`d458ec8`).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Công cụ:** Claude Code (Claude Opus 5.5) trong VS Code.
- **Dùng vào:** đọc đề (cả hai file `.docx`) và repo; đề xuất phân vai, thứ tự làm việc; chỉ lệnh cài môi trường cho Windows PowerShell; soạn văn bản hồ sơ, `group_report.md` và báo cáo này; rà soát chéo file của nhóm (phát hiện lỗi phạm vi pilot, B4 lệch giữa 9 phút và phút trong dữ liệu, `lab13.py` chưa tính tỉ lệ `ok` theo từng lần chạy); tạo phiếu gắn nhãn trống chép từ đề.
- **Không dùng AI:** gắn nhãn 20 ca lỗi (phiếu trống không có đáp án, AI không nhận xét nhãn trước khi so với người gắn nhãn 1); không lấy con số nào từ AI, mọi số trong hồ sơ lấy từ output `python lab13.py` hoặc file của nhóm.
- **Cách tự kiểm tra:** tự chạy lệnh cài đặt và thấy `san sang`, `lab13.py` báo `NotImplementedError` đúng như đề mô tả trước khi viết hàm. Các kiểm tra sau chạy trong phiên Claude Code, mình xem output: chạy lại `python lab13.py` và so từng số trong hồ sơ; `yaml.safe_load` và tìm dấu `?` cho `pilot_plan.yaml`; tìm từ cấm trong `report/team`; script so 20/20 nhãn giữa phiếu gốc và file nộp. Phần phải tự nắm để trả lời hội đồng: vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, cách tính hệ số thiết kế và cỡ mẫu hiệu dụng khi chia theo cụm, lý do của đề xuất.

## 6. Tự đánh giá

- **Làm được:** hồ sơ được điền dần từ đầu buổi nên không dồn việc đến 16:36; mỗi mục có con số, trạng thái và một vai trò phụ trách; phát hiện và sửa mâu thuẫn phạm vi pilot trước khi duyệt chéo.
- **Chưa tốt:** mất thời gian đầu buổi vì chạy lệnh macOS trên Windows; dựa nhiều vào AI cho phần soạn văn bản và rà soát, nên cần tự luyện giải thích công thức cỡ mẫu theo cụm và lý do đề xuất bằng lời của mình.
- **Lần sau:** đọc kỹ hướng dẫn theo đúng hệ điều hành trước buổi lab; tự tính tay ít nhất một con số ở mỗi CP thay vì chỉ đối chiếu output.
