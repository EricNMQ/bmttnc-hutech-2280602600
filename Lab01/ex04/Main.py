from QuanLySinhVien import QuanLySinhVien


def nhap_thong_tin():
    ten = input("Họ tên: ").strip()
    gioi_tinh = input("Giới tính: ").strip()
    chuyen_nganh = input("Chuyên ngành: ").strip()
    diem = float(input("Điểm trung bình: ").replace(",", "."))
    if not 0 <= diem <= 10:
        raise ValueError("Điểm phải từ 0 đến 10.")
    return ten, gioi_tinh, chuyen_nganh, diem


def hien_thi(danh_sach):
    if not danh_sach:
        print("Không có sinh viên.")
        return
    print("ID | Họ tên | Giới tính | Chuyên ngành | Điểm | Học lực")
    for sinh_vien in danh_sach:
        print(sinh_vien)


def main():
    quan_ly = QuanLySinhVien()
    while True:
        print("""
1. Thêm sinh viên
2. Cập nhật sinh viên theo ID
3. Xóa sinh viên theo ID
4. Tìm sinh viên theo tên
5. Sắp xếp theo điểm giảm dần
6. Sắp xếp theo chuyên ngành
7. Hiển thị danh sách
0. Thoát""")
        lua_chon = input("Chọn chức năng: ").strip()
        try:
            if lua_chon == "0":
                break
            if lua_chon == "1":
                sinh_vien = quan_ly.them(*nhap_thong_tin())
                print(f"Đã thêm sinh viên ID {sinh_vien.id}.")
            elif lua_chon == "2":
                sinh_vien = quan_ly.tim_theo_id(int(input("ID cần cập nhật: ")))
                if sinh_vien is None:
                    print("Không tìm thấy ID.")
                else:
                    sinh_vien.cap_nhat(*nhap_thong_tin())
                    print("Đã cập nhật sinh viên.")
            elif lua_chon == "3":
                if quan_ly.xoa(int(input("ID cần xóa: "))):
                    print("Đã xóa sinh viên.")
                else:
                    print("Không tìm thấy ID.")
            elif lua_chon == "4":
                hien_thi(quan_ly.tim_theo_ten(input("Tên cần tìm: ").strip()))
            elif lua_chon == "5":
                quan_ly.sap_xep_theo_diem()
                hien_thi(quan_ly.danh_sach)
            elif lua_chon == "6":
                quan_ly.sap_xep_theo_chuyen_nganh()
                hien_thi(quan_ly.danh_sach)
            elif lua_chon == "7":
                hien_thi(quan_ly.danh_sach)
            else:
                print("Lựa chọn không hợp lệ.")
        except ValueError:
            print("Dữ liệu không hợp lệ. ID phải là số nguyên và điểm phải từ 0 đến 10.")


if __name__ == "__main__":
    main()
