cac_phan_tu = tuple(input("Nhập các phần tử, cách nhau bằng dấu cách: ").split())
if cac_phan_tu:
    print("Phần tử đầu tiên:", cac_phan_tu[0])
    print("Phần tử cuối cùng:", cac_phan_tu[-1])
else:
    print("Tuple rỗng.")
