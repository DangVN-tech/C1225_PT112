# Bai tap 1
#def pow(a):
#    return a**2
#print(pow(int(input("Nhap mot so nguyen: "))))

# Bai tap 2
#def dientich(r):
#    return 3.14*r**2
#def chuvi(r):
#    return 3.14*r*2
#r=int(input("Nhap Ban kinh: "))
#print("Dien tich: ", dientich(r))
#print("Chu vi: ", chuvi(r))

# Bai tap 3
#def giaithua(a):
#    tich=1
#    for i in range(1,a+1):
#        tich=tich*i
#    return tich
#a=int(input("Nhap mot so nguyen: "))
#print(giaithua(a))

# Bai tap 5
#def so_nho_nhat(a,b,c):
#    if a<b and a<c:
#        return a
#    elif a>b and a<c:
#        return b
#    else:
#        return c
#a=int(input("Nhap so thu nhat: "))
#b=int(input("Nhap so thu hai: "))
#c=int(input("Nhap so thu ba: "))
#nho_nhat=so_nho_nhat(a,b,c)
#print(f"So nho nhat la: {nho_nhat}")

# Bai tap 7
def Tong(a):
    M=0
    for i in range(0,a+1):
        if i%2==0:
            M=M+i
        else:
            continue
    return M
a=int(input("Nhap mot so nguyen: "))
print("Tong tat ca cac so chan:", Tong(a))