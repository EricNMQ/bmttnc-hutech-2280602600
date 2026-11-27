cac_so = input("Nhập các số nhị phân 4 bit, cách nhau bằng dấu phẩy: ")
ket_qua = []
for so in cac_so.split(","):
    so = so.strip()
    if len(so) == 4 and all(bit in "01" for bit in so) and int(so, 2) % 5 == 0:
        ket_qua.append(so)
print(",".join(ket_qua))
