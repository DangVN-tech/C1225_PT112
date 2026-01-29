 ### Quan ly san pham ###
choice = 0


while choice !=5:
    print("=== Chuong trinh quan ly Ban be ===")
    print("Nhap phim 1 de hien thi Danh sach San pham")
    print("Nhap phim 2 de Them moi San pham")
    print("Nhap phim 3 de Xoa San pham")
    print("Nhap phim 4 de Sua ten San pham")
    print("Nhap phim 5 de thoat khoi chuong trinh")
    choice=int(input("=== Vui long nhap yeu cau: "))
    if choice==1: 
        print(Friendlist)
    elif choice==2:
        x=print(input("vui long Them ten Ban moi: "))
        Friendlist.append(x)
        print("Da Them ban moi thanh cong")
    elif choice==3:
        y=print("Nhap ten Ban be muon xoa: ")
        Friendlist.pop(y)
    elif choice==4:
        z=print
    elif choice==5:
        print("Da thoat khoi chuong trinh")
        break
    else:
        print("Nhap so khong chinh xac. Vui long nhap lai !!")