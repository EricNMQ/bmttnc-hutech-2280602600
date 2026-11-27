def dao_nguoc(chuoi):
    return chuoi[::-1]


if __name__ == "__main__":
    chuoi = input("Nhập chuỗi: ")
    print(dao_nguoc(chuoi))
