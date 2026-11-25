# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Dota
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có mở pilot hay không. Hồ sơ trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào để ra được quyết định.

Cách làm: mọi con số do `src/lab13.py` tính từ hai file trace (1.200 yêu cầu, 1.624 lần chạy), đối chiếu với slide chữa sau mỗi checkpoint. Mỗi thành viên làm trên nhánh riêng rồi mở pull request vào `main`; mỗi file hồ sơ chỉ một người sửa để tránh xung đột.

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): `mo_hinh` cộng token, tool của mọi lần chạy (kể cả lần lỗi) và phút xem lại, làm lại (`simulated`), chia cho số việc thành công; chạy lại cho từng loại yêu cầu (A3) và cộng chi phí cố định (A4).
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): mỗi kịch bản là một lần gọi `mo_hinh` với một tham số đã đổi; B3 tính thêm chi phí cả hệ thống cho phần nhân viên làm thay.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): ...
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): ...
- **E · Chỉ số, event, rủi ro** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): ...

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** (`simulated`), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu; giờ nhân viên chiếm 92,5% tổng chi phí.
- So với nhân viên tự làm (12.000 đ): cả hệ thống **5.865 đ/yêu cầu = 0,49×** (`simulated`); `quoc_te` 1,88× nên loại khỏi phạm vi.
- Yếu tố nhạy nhất: số ca làm lại (+51,8% khi gấp đôi), tỉ lệ xem lại (+40,7%), lương (+23,1%) (`simulated`).
- Con số bất lợi: xem lại 100% làm chi phí lên 0,98–1,04× (`simulated`).
- Đề xuất cuối của `ho_so_launch_v0.md`: ...
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ...

## 5. Khó khăn và cách xử lý

- **Cài môi trường trên Windows.** Chạy nguyên khối lệnh macOS/Linux trong `src/README.md` bằng Windows PowerShell báo lỗi `python3 : The term 'python3' is not recognized...` và `source : The term 'source' is not recognized...`. Xử lý: dùng lệnh Windows `python -m venv .venv` rồi `.\.venv\Scripts\Activate.ps1`; sau đó `python -m pip install -r requirements.txt` cài xong (pandas 3.1.1, statsmodels 0.15.0, Python 3.12.10) và `python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"` in `san sang`.
- **B4 lệch giữa giả định đề và dữ liệu.** Đề cho 9 phút mỗi ca làm lại, nhưng cột `phut_lam_lai_simulated` trung bình 15,3 phút/ca trên toàn mẫu và 16,25 phút/ca trong phạm vi. Nhóm báo cáo cả ba con số (11.743 đ, 12.414 đ, 12.516 đ, đều `simulated`) thay vì chọn một.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

| Thành viên | Vai | Phần chính |
| --- | --- | --- |
| Phùng Quang Trà | Nhóm trưởng · gắn nhãn 2, kiêm giữ hồ sơ | `TEAM.md`, `ho_so_launch_v0.md`, `group_report.md`, gắn nhãn CP3 |
| Trần Văn Tuấn | Viết code CP1–CP2 → kiểm số CP4–CP5 | `src/lab13.py` A, B; luật dừng; rủi ro E2 |
| Lại Trọng Đức | Kiểm số CP1–CP2 → viết code CP4–CP5 | `bang_chi_phi.md`; D1, E1; `pilot_plan.yaml` |
| Nguyễn Bảo Trung | Gắn nhãn 1 | `bang_loi.md`, danh sách event trong `chi_so.md`, `phieu_cham.md` |

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; pilot phải thay bằng phút đo thật từ event.
- Dữ liệu chỉ là mẫu 1.200 yêu cầu từ 6 depot trong 2 tuần chạy thử, không có nhóm đối chứng, nên chỉ nói "chỉ số trong đợt chạy thử là …".
- ...

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359.
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com.
- Tài liệu statsmodels, lớp `NormalIndPower` (mục `stats.power`).
- Tài liệu lab: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
