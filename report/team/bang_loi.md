# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Bảo Trung · Người gắn nhãn 2: Phùng Quang Trà (gắn trong 8 phút, không trao đổi; bộ nhãn gốc của người 2 lưu tại `report/team/cp3_nhan_doc_lap_nguoi_2.md`, không sửa lại sau khi so)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Hệ thống | Do người dùng | Không | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Ngầm | Hệ thống | Không | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 16 / 20 = 80% (đạt ngưỡng ≥ 80%)

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 1 (Do người dùng vs Hệ thống → Do người dùng):** Gắn nhãn theo nguyên nhân gốc làm phát sinh lỗi (khách nhập thiếu 2 chữ số tài khoản), không gắn theo chỗ cần sửa (thêm kiểm tra định dạng ở hệ thống).
- **Ca 3 (Hệ thống vs Ngữ cảnh → Ngữ cảnh):** Khi đề nêu rõ trợ lý làm đúng thiết kế (hoàn về ví LogiX) nhưng giả định đó lệch kỳ vọng của khách (chờ về tài khoản ngân hàng) thì là **Ngữ cảnh**, không phải **Hệ thống**.
- **Ca 8 (Ngầm vs Hệ thống → Hệ thống):** Bịa điều khoản không có trong chính sách ("Điều 7.2") ngay trong câu trả lời là lỗi **Hệ thống** (trả lời sai so với chính sách); chỉ gắn **Ngầm** khi sai sót âm thầm kéo dài mà cả người dùng lẫn hệ thống đều không phát hiện ra (như ca 5, 12, 17).
- **Ca 13 (Hệ thống vs Giới hạn hệ thống → Giới hạn hệ thống):** Khi nguyên nhân gốc là câu hỏi nằm ngoài phạm vi trợ lý (bảo hiểm hàng hoá của đối tác) thì gắn **Giới hạn hệ thống**, dù cách trợ lý trả lời chung chung cũng chưa tốt.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 14 | Do người dùng | Theo dõi hằng ngày các ca có `ticket_mo_lai` trong 24 giờ sau `ticket_dong` với lý do "chưa nhận tiền", đối chiếu trạng thái chuyển tiền từ ngân hàng/ví; cảnh báo khi vượt 0,5% tổng đơn đóng trong tuần. | Thêm hộp thoại xác nhận 2 bước kèm số tiền & mã giao dịch trước khi đóng, cho phép khách hoàn tác/mở lại trong 24 giờ nếu đối soát chưa thấy giao dịch thành công. | PM sản phẩm ứng dụng khách hàng |
| 7 | Hệ thống | Cảnh báo tức thời (ngưỡng > 0 ca/ngày) khi cùng `trace_id` có `agent_lan_chay_xong` với `status = loi` ở lần thử cuối nhưng vẫn phát sinh `ticket_dong` (`ket_qua = thanh_cong`) hoặc thông báo hoàn tiền thành công. | Khoá cứng quy trình: chỉ gửi thông báo thành công khi sổ cái trả về mã xác nhận ghi sổ; nếu lỗi 503 sau khi hết số lần thử thì chuyển trạng thái thất bại và phát event `chuyen_nhan_vien` kèm tóm tắt. | Kỹ sư backend phụ trách trợ lý hoàn phí |
| 16 | Ngữ cảnh | Theo dõi hằng tuần số thông báo Zalo có `closed_at` (từ `ticket_dong`) rơi vào khung 22:00–07:00 (ngưỡng > 0 ca/tuần sau khi áp quy tắc giờ gửi) kết hợp tỉ lệ phản ánh/chặn OA Zalo vượt 0,2%/tuần. | Đặt khung giờ yên lặng 22:00–07:00 cho kênh Zalo: vẫn xử lý và ghi nhận hoàn tiền ngay, nhưng giữ thông báo lại để gửi vào 07:00 sáng hôm sau (hoặc chỉ hiện trong lịch sử ứng dụng theo tuỳ chọn của khách). | PM trợ lý hoàn phí |
| 4 | Giới hạn hệ thống | Theo dõi hằng tuần event `chuyen_nhan_vien` nối với `yeu_cau_tao` qua `trace_id`, gom theo `loai = quoc_te` và `ly_do = thieu_du_lieu_doi_tac`; cảnh báo nếu > 0 ca `quoc_te` vẫn lọt vào luồng trợ lý sau khi bật bộ lọc phạm vi. | Đặt luật định tuyến tại đầu vào: chuyển thẳng toàn bộ đơn `loai = quoc_te` sang hàng đợi nhân viên ngay khi phát sinh `yeu_cau_tao`, không cho trợ lý chạy thử tốn token, và báo rõ cho khách là nhân viên chuyên trách đang xử lý. | Kỹ sư hệ thống ticket (định tuyến đầu vào) |
| 5 | Ngầm | Chạy kiểm mẫu hằng tuần qua event `kiem_tra_mau_hoan_tien` (ưu tiên phân tầng đơn có mã giảm giá, so `so_tien_da_hoan` với `so_tien_dung` qua `trace_id`), kèm đối chiếu tự động hằng ngày với số tiền thực thu; cảnh báo khi > 0 ca hoàn vượt thực thu hoặc tỉ lệ lệch mẫu > 0,5%/tuần. | Sửa tool tính hoàn tiền để lấy số tiền thực thu sau giảm giá làm gốc, đặt luật chặn cứng `so_tien_da_hoan <= so_tien_thuc_thu` tại dịch vụ sổ cái, và bổ sung kiểm thử tự động cho các kịch bản mã giảm giá trước bước mở rộng pilot tiếp theo. | Kỹ sư phụ trách dịch vụ sổ cái hoàn tiền |
