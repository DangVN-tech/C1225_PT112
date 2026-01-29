# Bai tap 1
#a= int(input("Nhap vao mot so nguyen duong: "))
#M=1
#for i in range (1,a+1):
#    M=M*i
#print(f"Giai thua cua {a} la: ", M)

# Bai tap 2
#a= str(input("Nhap vao mot chuoi: "))
#for i in a:
#    print(i, end="-")

# Bai tap 3
#a= int(input("Nhap vao mot so nguyen duong: "))
#S=0
#for i in range (1,a):
#    if a%i==0:
#        S=S+i
#if S==a:
#    print(f"{a} la so hoan hao")
#else:
#    print(f"{a} Khong la so hoan hao")

# Bai tap 4
#a= int(input("Nhap so nguyen duong Thu Nhat: "))
#b= int(input("Nhap so nguyen duong Thu Hai: "))
#Suma=0
#for i in range(1,a):
#    if a%i==0:
#        Suma+=i
#    else:
#        continue
#Sumb=0
#for j in range(1,b):
#    if b%j==0:
#        Sumb+=j
#    else:
#        continue
#if Sumb==a and Suma==b:
#    print("Hai so than thiet nhau")
#else:
#    print("Hai so khong than thiet nhau")

# Bai tap 5
#import random
#R = random.randint(100,999)
#R1= R//100
#R2= R//10-R1*10
#R3= R-R1*100-R2*10
#for x in range(1,10):
#    if x==R1:
#        print (f"Mat khau so dau: {x}")
#    for y in range (1,10):
#        if y==R2:
#            print (f"Mat khau so giua: {y}")
#        for z in range (1,10):
#            if z==R3:
#                print (f"Mat khau so cuoi: {z}")
#print(f"Password found: {x,y,z}")
