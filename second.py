diem_thi = float(input("Nhập điểm thi của bạn: "))
diem_thi_max = 10.0

if(diem_thi >= 9 and diem_thi <= diem_thi_max):
    print("Xuất sắc!")
elif(diem_thi >= 7 and diem_thi < 9):
    print("Khá")
elif(diem_thi >= 5 and diem_thi < 7):
    print("Đạt")
elif(diem_thi >= 0 and diem_thi < 5):
    print("Chưa đạt!")
else:
    print("Có gì đó sai sai!")