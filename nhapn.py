dk= True
while dk:
    try:
        n=int(input("nhập n"))
        if n>0:
            break
    except ValueError:
        print("Loi du lieu!")

i=1
while i<=n:
    print(f"{i}",end="")
    i+=1
