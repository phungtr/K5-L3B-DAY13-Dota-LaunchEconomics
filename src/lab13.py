"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

YEU_CAU_MOI_THANG = 45000     # A4: khối lượng đầy đủ của LogiX-VN
CHI_PHI_CO_DINH = 40_000_000  # A4: đồng mỗi tháng
PHAM_VI = ['noi_dia', 'hang_nang']  # phạm vi pilot


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


# ---------- Nhiệm vụ A3 · Tách theo loại; A4 · Chi phí cố định ----------
def bang_theo_loai(runs, reqs):
    """A3: mỗi loại yêu cầu một dòng."""
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        dong.append(dict(loai=loai, so_yc=len(sub),
                         ti_le_thanh_cong=kq['thanh_cong'] / len(sub),
                         lan_chay_moi_yc=runs[runs['request_id'].isin(sub['request_id'])].shape[0] / len(sub),
                         cps=kq['cps'], so_voi_12000=kq['cps'] / BASELINE))
    return pd.DataFrame(dong)


def chi_phi_co_dinh_pilot(runs, reqs):
    """A4: cộng chi phí cố định 40 triệu/tháng vào phạm vi noi_dia + hang_nang."""
    sub = reqs[reqs['loai'].isin(PHAM_VI)]
    kq = mo_hinh(runs, sub)
    ket = []
    for ten, khoi_luong in [('45.000 yêu cầu/tháng', YEU_CAU_MOI_THANG),
                            ('Một nửa khối lượng', YEU_CAU_MOI_THANG / 2)]:
        thanh_cong_thang = khoi_luong * kq['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = CHI_PHI_CO_DINH / thanh_cong_thang
        tong = kq['cps'] + co_dinh_moi_viec
        ket.append(dict(khoi_luong=ten, viec_thanh_cong_thang=thanh_cong_thang,
                        co_dinh_moi_viec=co_dinh_moi_viec, cps_cong_co_dinh=tong,
                        so_voi_12000=tong / BASELINE))
    return pd.DataFrame(ket)


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
KICH_BAN_B1 = {
    'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
    'Lương tăng 25%':           dict(luong_phut=2500),
    'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
    'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
}


def bang_do_nhay(runs, reqs):
    """B1: đổi từng yếu tố, so với gốc A2. Trả về DataFrame."""
    goc = mo_hinh(runs, reqs)['cps']
    dong = []
    for ten, kw in KICH_BAN_B1.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi_pct=(cps / goc - 1) * 100))
    return pd.DataFrame(dong)


def kich_ban_cap(runs, reqs):
    """B2: giá token gấp đôi cùng lúc với xem lại gấp đôi."""
    return mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']


def gioi_han_chay(runs, reqs):
    """B3: giới hạn số lần chạy, tính cả chi phí cho nhân viên làm thay."""
    dong = []
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_thanh_cong = int(len(reqs) - kq['thanh_cong'])
        ca_he_thong = kq['tong'] + BASELINE * khong_thanh_cong
        dong.append(dict(gioi_han=gioi_han, tong_tro_ly=kq['tong'],
                         khong_thanh_cong=khong_thanh_cong,
                         ca_he_thong=ca_he_thong, cps=kq['cps']))
    return pd.DataFrame(dong)


def xem_lai_tat_ca(runs, reqs):
    """B4: xem lại 100% ca noi_dia + hang_nang (5 phút mỗi yêu cầu có ít nhất một lần chạy ok)."""
    sub = reqs[reqs['loai'].isin(PHAM_VI)].copy()
    co_ok = runs[runs['status'] == 'ok']['request_id'].unique()
    sub['phut_xem_lai_simulated'] = sub['request_id'].isin(co_ok) * 5
    kq = mo_hinh(runs, sub)
    return kq['cps'], kq['cps'] / BASELINE


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')

    # CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\nA3 · theo loại')
    print(bang_theo_loai(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.3f}'))

    # CP1 · Nhiệm vụ A4: chi phí cố định cho phạm vi noi_dia + hang_nang.
    print('\nA4 · chi phí cố định (phạm vi noi_dia + hang_nang)')
    print(chi_phi_co_dinh_pilot(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.2f}'))

    # CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    print('\nB1 · đổi từng yếu tố')
    print(bang_do_nhay(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.1f}'))
    print(f'\nB2 · giá token gấp đôi + xem lại gấp đôi: {kich_ban_cap(runs, reqs):,.0f} đ')

    print('\nB3 · giới hạn số lần chạy')
    print(gioi_han_chay(runs, reqs).to_string(index=False, float_format=lambda x: f'{x:,.0f}'))

    cps_b4, ti_so_b4 = xem_lai_tat_ca(runs, reqs)
    print(f'\nB4 · xem lại 100% (noi_dia + hang_nang): {cps_b4:,.0f} đ = {ti_so_b4:.2f}× [simulated]')

    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
