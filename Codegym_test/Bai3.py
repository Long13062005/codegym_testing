# Quan ly sinh vien
# Khai bao struct SinhVien gom ten , diem toan , ly , hoa. nhap danh sach n sinh vien
# # Khai bao N
N = int(input("Input N: "))
# # Kiem tra N > 0
while N <= 0:
    N = int(input("Input N > 0 : "))


# Khai bao struct sinh vien
class SinhVien:
    def __init__(self, ten, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa


# # Khai bao danh sach sinh vien
sinh_vien_list = []
# CheckDiemHopLe
def checkDiemHopLe(diem):
    if diem < 0 or diem > 10 :
        return False
    return True
# Check Nhap diem toan
def checkDiemToan(diem_toan):
    while not checkDiemHopLe(diem_toan):
        diem_toan = float(input("Input lai diem toan [0-10]: "))
    return diem_toan
# Check Nhap diem ly
def checkDiemLy(diem_ly):
    while not checkDiemHopLe(diem_ly):
        diem_ly = float(input("Input lai diem ly [0-10]: "))
    return diem_ly
# Check Nhap diem hoa
def checkDiemHoa(diem_hoa):
    while not checkDiemHopLe(diem_hoa):
        diem_hoa = float(input("Input lai diem hoa [0-10]: "))
    return diem_hoa
# # Nhap danh sach sinh vien
for i in range(N):
    ten = input("Input ten sinh vien {}: ".format(i + 1))
    diem_toan = float(input("Input diem toan: "))
    diem_toan = checkDiemToan(diem_toan)
    diem_ly = float(input("Input diem ly: "))
    diem_ly = checkDiemLy(diem_ly)
    diem_hoa = float(input("Input diem hoa: "))
    diem_hoa = checkDiemHoa(diem_hoa)
    sinh_vien = SinhVien(ten, diem_toan, diem_ly, diem_hoa)
    sinh_vien_list.append(sinh_vien)


# # Tim sinh vien co diem trung binh cao nhat
def tinh_trung_binh(sinh_vien):
    return (sinh_vien.diem_toan + sinh_vien.diem_ly + sinh_vien.diem_hoa) / 3

# In ra cac sinh vien co diem TB >= 8

for sinh_vien in sinh_vien_list:
    if tinh_trung_binh(sinh_vien) >= 8:
        print("Sinh vien co diem TB >= 8: ", sinh_vien.ten)
