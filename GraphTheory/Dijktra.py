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

def dijkstra(dt):
    for dong in dt:
        for dia_chi in range(len(dong)):
            if  dia_chi != 0:
                pass
    pass

def xuly():
    pass

if __name__ == "__main__":
    dijkstra(tap_do_thi_tu_tap_tin())