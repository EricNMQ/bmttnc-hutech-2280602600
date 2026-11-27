from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.danh_sach = []

    def them(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        sinh_vien = SinhVien(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)
        self.danh_sach.append(sinh_vien)
        return sinh_vien

    def tim_theo_id(self, ma):
        for sinh_vien in self.danh_sach:
            if sinh_vien.id == ma:
                return sinh_vien
        return None

    def xoa(self, ma):
        sinh_vien = self.tim_theo_id(ma)
        if sinh_vien is None:
            return False
        self.danh_sach.remove(sinh_vien)
        return True

    def tim_theo_ten(self, ten):
        return [sv for sv in self.danh_sach if ten.casefold() in sv.ten.casefold()]

    def sap_xep_theo_diem(self):
        self.danh_sach.sort(key=lambda sv: sv.diem_trung_binh, reverse=True)

    def sap_xep_theo_chuyen_nganh(self):
        self.danh_sach.sort(key=lambda sv: sv.chuyen_nganh.casefold())
