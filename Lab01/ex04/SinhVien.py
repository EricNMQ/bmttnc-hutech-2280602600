class SinhVien:
    _id_tiep_theo = 1

    def __init__(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.id = SinhVien._id_tiep_theo
        SinhVien._id_tiep_theo += 1
        self.cap_nhat(ten, gioi_tinh, chuyen_nganh, diem_trung_binh)

    def cap_nhat(self, ten, gioi_tinh, chuyen_nganh, diem_trung_binh):
        self.ten = ten
        self.gioi_tinh = gioi_tinh
        self.chuyen_nganh = chuyen_nganh
        self.diem_trung_binh = diem_trung_binh

    def hoc_luc(self):
        if self.diem_trung_binh >= 8:
            return "Giỏi"
        if self.diem_trung_binh >= 6.5:
            return "Khá"
        if self.diem_trung_binh >= 5:
            return "Trung bình"
        return "Yếu"

    def __str__(self):
        return (f"{self.id} | {self.ten} | {self.gioi_tinh} | {self.chuyen_nganh}"
                f" | {self.diem_trung_binh:g} | {self.hoc_luc()}")
