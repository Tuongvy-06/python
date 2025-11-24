while True:
    try:
        n =int(input("nhập n:"))
        if n<=0:
            print("n phải lớn hơn 0 ,nhập lại!")
            continue
        break
    except ValueError:
        print("lỗi: phải nhập số nguyên!")

print("====Cau1====")
for i in range(1,n + 1):
    if i % 2 ==0:
        print(i, end="")
print("====Cau2====")
Tong=0
for i in range(1,n + 1):
    if(i % 2!=0):
        Tong += i
print(f"Tong so le tu 1 den {n} la: {Tong}")
print("====Cau3====")
Dem=0
for i in range(1,n + 1):
    if(i % 3==0):
        Dem +=1
print("Có", Dem,"số chia hết cho 3 trong đoạn {1,",n,"}")
print("====Cau4====")
Dem_am=0
for i in range(10):
    i=float(input("Nhập số thứ{}:".format(i+1)))
    if i<0:
        Dem_am+=1
print("Có",Dem_am, "Số âm trong 10 số đã nhập")
print("====Cau5====")
n =int(input("nhập n:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)

print("====Cau6====")
n =int(input("nhập n:"))
for i in range(1, n+1):
    if i ==5:
        continue
    print(i,end="")

print("====Cau8====")
while True:
    try:
        n =int(input("nhập n:"))
        if n>=0:
            break
    except ValueError:
        print("Lỗi nhập dữ liệu")
i=1
max= -1000
min= 1000
while(i<=n):
    try:
        so=int(input(f"Nhap so thu {i} :"))
        i+=1
        if(so>max):
            max = so
        if(so<min):
            min = so
    except ValueError:
        print("Sai dữ liệu")
print(f"Giá trị lớn nhất là{max},nhỏ nhất là{min}")
print("====Cau9====")
so = int(input("Nhập số:"))
So=so
Dem=0
while(so!=0):
    so=so//10
    Dem +=1
print(f"So{So} co {Dem} chu")





