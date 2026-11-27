cac_so = [int(so) for so in input("Nhập các số nguyên, cách nhau bằng dấu cách: ").split()]
print("Tổng các số chẵn:", sum(so for so in cac_so if so % 2 == 0))
