# Bai tap 1
#a = float(input("Nhap vao So luong Nhan vien: "))
#if a>15000000:
#    print("Luong rong = ", a*0.7)
#elif a>7000000:
#    print("Luong rong = ", a*0.8)
#else:
#    print("Luong rong = ", a*0.9)

# Bai tap 2
#print("Cho phuong trinh bac 2 co dang: a*x**2+b*x+c")
#a = float(input("Nhap vao Bien so a: "))
#b = float(input("Nhap vao Bien so b: "))
#c = float(input("Nhap vao Bien so c: "))
#str_a= str(a)
#str_b= str(b)
#str_c= str(c)
#print(f"Phương trinh bac 2 co dang: {str_a}*x**2+{str_b}*x+{c}")
#if a==0 and b==0:
#    print("Phuong trinh vo nghiem")
#elif a==0:
#    print("Phuong trinh co 1 nghiem la:", -c/b)
#elif b**2-4*a*c<0:
#    print("Phuong trinh vo nghiem")
#else:
#    delta=b**2-4*a*c
#    print("Phuong trinh co 2 nghiem", (-b+delta**0.5)/(2*a), (-b-delta**0.5)/(2*a))

# Bai tap 3
#a = float(input("Nhap vao So Doanh so ban hang: "))
#if a<=100000000:
#    print("Hoa hong = ", a*0.05)
#elif a<=300000000:
#    print("Hoa hong = ", a*0.1)
#else:
#    print("Hoa hong = ", a*0.2)

# Bai tap 4
#a = float(input("Nhap vao So Doanh so ban hang: "))
#if a<=100000000:
#    print("Hoa hong = ", a*0.05)
#elif a<=300000000:
#    print("Hoa hong = ", a*0.1)
#else:
#    print("Hoa hong = ", a*0.2)

# Bai tap 5
a = float(input("Nhap vao so phut goi dien: "))
thuebao = 25000
if a<=50:
    print("Cuoc dien thoai =", thuebao+600*a)
elif 50<a<=200:
    print("Cuoc dien thoai =", thuebao+600*50+400*a)
else:
    print("Cuoc dien thoai =", thuebao+200*a)

# Bai tap 6
#a = int(input("Nhap vao 1 so nguyen: "))
#if a%3==0 and a%5!=0:
#    print("Fizz")
#elif a%3!=0 and a%5==0:
#    print("Buzz")
#elif a%3==0 and a%5==0:
#    print("Fizz-Buzz")
#else:
#    print(a)