# Bai tap 1
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
if a%b==0:
    print("a chia het cho b")
else:
    print("a khong chia het cho b")

# Bai tap 2
a = int(input("Nhap so tuoi: "))
if a>6:
    print("Du tuoi di hoc")
else:
    print("Chua du tuoi di hoc")

# Bai tap 3
a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
c = int(input("Nhap so nguyen thu ba: "))
if a>b:
    if a>c:
        print("a la so lon nhat")
    else:
        print("c la so lon nhat")
else:
    if b>c:
        print("b la so lon nhat")
    else:
        print("c la so lon nhat")

# Bai tap 4
a = float(input("Nhap chieu cao ban Khang: "))
b = float(input("Nhap chieu cao Kha: "))
if a>b:
    print("Khang cao hon Kha")
else:
    print("Khang thap hon Kha")

# Bai tap 5
a = float(input("Nhap Diem thi cua hoc sinh: "))
if a>10 or a<0:
    print("Nhap sai so Diem thi")
elif a>=9:
    print("Xep loai A")
elif a>=7:
    print("Xep loai B")
elif a>=5:
    print("Xep loai C")
else:
    print("Xep loai D")

# Bai tap 6
a = float(input("Nhap Can nang (kg): "))
b = float(input("Nhap Chieu cao (met): "))
bmi = a/(b**2)
if bmi>=30:
    print("Obese")
elif bmi>=25:
    print("Overweigth")
elif bmi>=18.5:
    print("Normal")
else:
    print("Underweight")

# Bai tap 7
a = int(input("Nhap so nam: "))
if a%4==0 and a%100!=0:
    print("Nam nhuan")
elif a%100==0 and a%400==0:
    print("Nam nhuan")
else:
    print("Khong la Nam nhuan")