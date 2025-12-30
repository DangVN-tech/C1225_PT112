# Bai tap 1
#for i in range (2,10):
#    for j in range(1,10):
#        print(f"{i}*{j}=",i*j, end="; ")
#    print()

# Bai tap 2
#a=int(input("Nhap vao so nguyen duong: "))
#count=2
#while count>=2 and count<a:
#    if a%count==0:
#        print("Day khong phai la so nguyen to")
#        break
#    count+=1
#else:
#    print("Day la so nguyen to")

# Bai tap 3
#import random
#x = random.randint(0,10)
#count=1
#a=1
#while count<=3:
#    a=int(input("Nhap vao so nguyen duong: "))
#    if a<x:
#        print("Goi y: So du doan Nho hon So bi mat")
#    elif a>x:
#        print("Goi y: So du doan Lon hon So bi mat")
#    else:
#        print("Xin chuc mung. Ban du doan chinh xac!")
#        break
#    count+=1
#else:
#    print("Da het luot choi")

### BAI TAP VE HINH
# Bai tap 1
#for i in range (4):
#    for j in range (8):
#        print("*", end= " ")
#    print()

# Bai tap 2
for i in range (1,7):
    count=1
    if count==i:
        print("*", end= " ")
    count+=1
    print()
    