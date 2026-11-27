from math import isqrt


def la_so_nguyen_to(so):
    if so < 2:
        return False
    for uoc in range(2, isqrt(so) + 1):
        if so % uoc == 0:
            return False
    return True


if __name__ == "__main__":
    so = int(input("Nhập số nguyên: "))
    if la_so_nguyen_to(so):
        print(f"{so} là số nguyên tố.")
    else:
        print(f"{so} không phải là số nguyên tố.")
