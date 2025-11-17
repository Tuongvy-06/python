try:
    Van=float(input("Nhap diem Van: "))
    Toan=float(input("Nhap diem Toan: "))
    Anh=float(input("Nhap diem Anh: "))
except ValueError:
    print("Loi sai du lieu!")
else:
    tb= (Van + Toan + Anh)/3
    if Van < 0 or Van > 10 or Toan < 0 or Toan > 10 or Anh < 0 or Anh > 10:
        print("Nhap diem khong hop le")
    else:
        if (tb>=9):
            print("Xếp loại xuất sắc")
        elif (tb>=8):
            print("Xếp loại Giỏi")
        elif (tb>=7):
            print("Xếp loại Khá")
        elif (tb>=5):
            print("Xếp loại Trung Bình")
        else:
            print("Xếp loại Yếu")