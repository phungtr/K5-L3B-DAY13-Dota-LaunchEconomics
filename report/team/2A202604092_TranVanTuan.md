# Báo cáo cá nhân — TranVanTuan-2A202604092

## 1. Thông tin thành viên

- Họ tên: Trần Văn Tuấn
- MSSV: 2A202604092
- Email: quyvangia2004@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người viết code CP1–CP2, sau đó là người kiểm số CP4–CP5

## 2. Phần việc phụ trách

- Người viết code CP1–CP2: `src/lab13.py` phần A1, `mo_hinh`, A3, A4, B1–B4.
- Người kiểm số CP4–CP5: đối chiếu D1 câu b và e; viết D2 và ba luật dừng trong `report/team/pilot_plan.yaml`.
- E2: ba dòng rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- **CP1 · A:** viết ba hàm kinh tế của việc chạy lại (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`). Ba phép thử đáp án biết trước đều ĐẠT. Viết `mo_hinh` tính chi phí trên mọi lần chạy, kể cả lần lỗi, chia cho số việc thành công. Kết quả: 4.472 đ mỗi việc thành công (simulated), gấp 16,3 lần hoá đơn token chia số yêu cầu. Viết A3 theo loại và A4 chi phí cố định (4.599 đ ở quy mô đầy đủ, simulated).
- **CP2 · B:** viết B1 (chín kịch bản đổi từng yếu tố), B2 (đổi cặp: 6.543 đ, +46,3%, đúng bằng tổng hai tác động riêng), B3 (giới hạn 2 lần rẻ nhất cho công ty, 6.901.220 đ), B4 (xem lại 100%: 1,04× so với nhân viên tự làm, simulated).
- **Kiểm số D1:** câu b, theo nhân viên m = 75, DE = 2,48, cần 3.103 yêu cầu mỗi nhóm = 42 người mỗi nhóm, tổng 84 > 40, không đủ người. Câu e, mức chênh 6 điểm với 20 nhân viên mỗi nhóm, m ≥ 299, DE = 6,96, n hiệu dụng 859.
- **D2 và luật dừng:** viết năm câu kiểm tra tách tác động (đối chứng cùng thời gian, ngẫu nhiên có seed, ảnh hưởng gián tiếp, chỉ số viết trước, 20 cụm mỗi nhóm). Viết ba luật dừng đủ bốn vế cho an toàn, chi phí và mức bỏ qua gợi ý.
- **Phát hiện khi kiểm số:** (a) chỉ số chính đo được là 82,83%, không khớp với baseline 0,70 đề bài dùng để tính cỡ mẫu; (b) cỡ mẫu 859 mỗi nhóm cần khoảng 11.960 yêu cầu trong phạm vi, tương đương khoảng 10 ngày toàn công ty, không khớp với đợt chạy thử 2 tuần nếu lịch rollout 1 tuần mỗi bước; (c) B4 có ba con số tuỳ giả định phút làm lại (11.743 · 12.414 · 12.516 đ), tôi dùng số đo thật trong trace (780 phút, 12.516 đ) và ghi cả hai trong bảng.
- **E2:** ba dòng rủi ro: ca làm lại tăng gấp đôi (+51,8%), tỉ lệ xem lại tăng gấp đôi (+40,7%), lương tăng 25% (+23,1%). Mỗi dòng có dấu hiệu đo được và vai trò phụ trách.
- **Lưu ý khi chạy trên Windows:** `lab13.py` in tiếng Việt lỗi với bảng mã cp1252 mặc định. Cần chạy `PYTHONUTF8=1 python lab13.py` hoặc đặt `chcp 65001`.

## 4. Bằng chứng

- Commit `20705cb`: `src/lab13.py` (CP1–CP2).
- Commit `dcdc852`: `report/team/pilot_plan.yaml` (D2, ba luật dừng, cỡ mẫu). Đã kiểm `yaml.safe_load` đọc được và không còn dấu `?` ngoài dòng chú thích.
- Commit `1110294`: `report/team/chi_so.md` (E2).
- Số kiểm tra: 4.472 đ, 978 việc thành công, 245.585 đ token, 84.000 đ tool, 1.780.000 đ xem lại và 2.264.000 đ làm lại (đều simulated trừ token và tool).

## 5. Công cụ AI đã dùng

- Claude Code (mô hình Claude của Anthropic) dùng để viết `src/lab13.py`, tính các con số, và soạn bản nháp cho `pilot_plan.yaml`, `chi_so.md` và báo cáo này.
- Cách kiểm tra: chạy `lab13.py` để xác nhận ba phép thử ĐẠT và các bảng A2–B4; tính lại D1 b, D1 e, tỉ lệ mở lại 4,25% và 3,97% bằng code; đối chiếu số trong bảng với `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`. Các số không khớp hướng dẫn (B4) được ghi rõ và giải thích trong báo cáo nhóm.

## 6. Tự đánh giá

- Tốt: số trong code khớp hướng dẫn ở A1–A4 và B1–B3. Kiểm được các con số bất lợi (baseline lệch, lịch pilot).
- Cần cải thiện: tôi chưa tự tay tính lại các con số ở CP1–CP2 trên giấy trước khi giao, nên cần tự kiểm lại trước khi nộp.
- (Phần này cần Tuấn tự viết lại bằng lời của mình.)
