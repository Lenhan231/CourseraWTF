import math
def tap_do_thi_tu_tap_tin():
    f = open("dijkstra.txt")
    so_dinh = int(f.readline().strip())
    cac_canh = f.readlines()
    f.close()
    
    dt = [[0 for _ in range(so_dinh)] for _ in range(so_dinh)]
    for canh in cac_canh:
        canh = canh.strip()
        ds_gia_tri = canh.split()
        if len(ds_gia_tri) != 3:
            continue
        dong = int(ds_gia_tri[0])
        cot = int(ds_gia_tri[1])
        khoang_cach = int(ds_gia_tri[2])
        dt[dong][cot] = khoang_cach
        dt[cot][dong] = khoang_cach
    return dt  

def duong_di(ds_dinh_truoc, dinh_dich):
    ds = [dinh_dich]
    dinh = dinh_dich 
    while True:
        dinh = ds_dinh_truoc[dinh]
        if dinh == None:
            break
        ds.insert(0, dinh)
    ds = [str(x) for x in ds]
    return '->'.join(ds)

def khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat):
    nho_nhat = math.inf
    for dinh in range(len(ds_khoang_cach)):
        if ds_khoang_cach[dinh] < nho_nhat and ds_dinh_cay_ngan_nhat[dinh] == False:
            nho_nhat = ds_khoang_cach[dinh]
            dinh_nho_nhat = dinh
    return dinh_nho_nhat

def dijkstra(do_thi, dinh_nguon):
    so_luong_dinh = len(do_thi)
    so_khoang_cach = [math.inf] * so_luong_dinh
    ds_khoan_cach[dinh_nguon] = 0
    ds_dinh_cay_ngan_nhat = [False] * so_luong_dinh
    ds_dinh_truoc = [None] * so_luong_dinh
    for i in range(so_luong_dinh):
        x = khoang_cach_ngan_nhat(ds_khoang_cach, ds_dinh_cay_ngan_nhat):
        

if __name__ == "__main__":
    duong_di(tap_do_thi_tu_tap_tin())