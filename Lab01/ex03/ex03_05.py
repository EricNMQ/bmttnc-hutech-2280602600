danh_sach = input("Nhập các phần tử, cách nhau bằng dấu cách: ").split()
so_lan = {}
for phan_tu in danh_sach:
    so_lan[phan_tu] = so_lan.get(phan_tu, 0) + 1
print(so_lan)
