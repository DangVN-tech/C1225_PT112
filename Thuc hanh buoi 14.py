# Bai tap 1 (Done)
#tuple=(1,2,3,4,5)
#print(tuple)
#print(tuple[0])
#print(tuple[4])

# Bai tap 2 (Done)
#t = (3, 7, 1, 9, 4)
#print(len(t))
#print(7 in t)

# Bai tap 3 (Done)
#animals = ("cat", "dog", "rabbit", "tiger")
#for i in animals:
#    print(i)

# Bai tap 4 (Done)
#numbers = (2, 4, 6, 8, 10)
#count=0
#for i in numbers:
#    count=count+i
#print(count)
#print("So lon nhat: ", max(numbers))
#print("So nho nhat: ", min(numbers))

# Bai tap 5 (Done)
#t = (1, 2, 3, 4, 5, 6, 7)
#print(t[0:3])
#print(t[2:4])

# Bai tap 6 (Done)
#t = (10, 20, 30, 40)
#l = list(t)
#l.append(50)
#t1=tuple(l)
#print(t1)

# Bai tap 7 (Done)
#students = (("An", 8.5),("Bình", 7.0),("Chi", 9.2))
#for i in students:
#    print(i)
#print("Hoc sinh diem cao nhat:", max(students))

# Bai tap 8
t = (1, 2, 2, 3, 2, 4, 5)
def solan(t,i)
for i in t:
    print(f"So lan so {i} xuat hien: ", t.count(i))
count=t.count(i)
if count>1:
    print(t.index(2))