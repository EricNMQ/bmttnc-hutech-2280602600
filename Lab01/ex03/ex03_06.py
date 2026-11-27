tu_dien = {}
so_muc = int(input("Nhập số mục của từ điển: "))
for _ in range(so_muc):
    khoa = input("Nhập khóa: ")
    tu_dien[khoa] = input("Nhập giá trị: ")

khoa = input("Nhập khóa cần xóa: ")
if khoa in tu_dien:
    del tu_dien[khoa]
else:
    print("Không tìm thấy khóa.")
print(tu_dien)
