# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | Chỉ số trong đợt chạy thử là 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | Chỉ số trong đợt chạy thử là 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % nhân viên dùng thật hằng tuần | Số `staff_id` có ít nhất 1 `nhan_vien_xem_lai` với `quyet_dinh_xem_lai = giu` trong tuần, chia số `staff_id` có ít nhất 1 `goi_y_hien_thi` trong tuần; báo cáo dạng k/n nhân viên mỗi tuần (đợt chạy thử có 20 nhân viên) và xem xu hướng, không đặt ngưỡng % cứng | Không cần tính |
| An toàn | Nhóm tự đề xuất: % gợi ý được giữ nguyên nhưng vẫn bị mở lại | Số yêu cầu có `quyet_dinh_xem_lai = giu` và có `ticket_mo_lai` trong 7 ngày, chia số yêu cầu có `quyet_dinh_xem_lai = giu` | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `yeu_cau_tao` | Hệ thống ticket | request_id, depot, loai, so_tien_vnd, created_at, trace_id | Khi yêu cầu hoàn phí vào hệ thống |
| `agent_lan_chay_xong` | Agent | run_id, request_id, attempt, tokens_in, tokens_out, tool_calls, status (`ok`/`loi`), trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `goi_y_hien_thi` | Giao diện nhân viên | request_id, staff_id, so_lan_chay, shown_at, trace_id | Khi gợi ý hiện cho nhân viên |
| `nhan_vien_xem_lai` | Nhân viên | staff_id, quyet_dinh_xem_lai (`giu`/`sua`/`bo`), phut_xem_lai đo từ shown_at đến lúc bấm, trace_id | Khi nhân viên bấm giữ / sửa / bỏ |
| `nhan_vien_lam_lai_xong` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong một ca trợ lý trả lời sai |
| `chuyen_nhan_vien` | Agent | request_id, so_lan_chay, ly_do, trace_id | Khi chạy hết 3 lần vẫn lỗi |
| `ticket_dong` | Hệ thống ticket | request_id, closed_at, ket_qua, trace_id | Khi yêu cầu được đóng |
| `ticket_mo_lai` | Khách / hệ thống ticket | request_id, reopened_at, ly_do, trace_id | Khi khách mở lại yêu cầu |
| `kiem_tra_mau_hoan_tien` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, trên mẫu ngẫu nhiên các yêu cầu đã đóng |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chính: `yeu_cau_tao.created_at` → `ticket_dong.closed_at` trong 24 giờ, không có `ticket_mo_lai` trong 7 ngày sau `closed_at`; mẫu số đếm `yeu_cau_tao`.
- Dùng (bỏ qua gợi ý): `nhan_vien_xem_lai` có `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia tổng số `nhan_vien_xem_lai`.
- An toàn (lỗi lọt đến khách): `ticket_mo_lai` trong 7 ngày, chia số `yeu_cau_tao`.
- Dùng (tự đề xuất): `goi_y_hien_thi` (mẫu số) và `nhan_vien_xem_lai` với `giu` (tử số), gom theo `staff_id` và tuần.
- An toàn (tự đề xuất): `nhan_vien_xem_lai` với `giu` (mẫu số) nối với `ticket_mo_lai` qua `trace_id` (tử số).
- Lỗi ngầm (hoàn sai tiền mà khách không mở lại): `kiem_tra_mau_hoan_tien` có `so_tien_da_hoan` khác `so_tien_dung`, chia số yêu cầu được kiểm trong tuần.
- Chi phí mỗi việc thành công (nhiệm vụ A) đo thật trong pilot: token, tool từ `agent_lan_chay_xong`; phút xem lại, phút làm lại từ `nhan_vien_xem_lai`, `nhan_vien_lam_lai_xong` (thay hai cột simulated); mẫu số là `ticket_dong` có `ket_qua = thanh_cong`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công `4.472 → 6.787 đ` (`+51,8%`, simulated) | Số `nhan_vien_lam_lai_xong` chia số `ticket_dong` có `thanh_cong`, theo tuần; `phut_lam_lai` đo thật | Nếu tỉ lệ làm lại tuần tăng so với tuần đầu pilot, rà 10 ca lỗi gần nhất tìm nguyên nhân gốc trước khi mở rộng | Trưởng nhóm CSKH |
| Tỉ lệ xem lại tăng gấp đôi | `4.472 → 6.292 đ` (`+40,7%`, simulated); giảm một nửa còn `3.562 đ` (`−20,3%`) | Số `nhan_vien_xem_lai` chia số `goi_y_hien_thi` theo tuần; `phut_xem_lai` đo từ `shown_at` | Giảm xem lại theo bậc khi chỉ số an toàn vẫn đạt; không xem 100% vì khi đó chi phí `1,04×` so với nhân viên tự làm (B4, simulated) | Giám đốc vận hành |
| Lương nhân viên tăng 25% | `4.472 → 5.506 đ` (`+23,1%`, simulated) | Đơn giá lương `2.500 đ` mỗi phút trong bảng chi phí hằng tháng | Cập nhật bảng chi phí khi có lương mới; so lại với ngưỡng `8.000 đ` trong luật dừng chi phí | Kế toán |
