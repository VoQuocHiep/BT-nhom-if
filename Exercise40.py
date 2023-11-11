a=int(input("Canh 1="))
b=int(input("Canh 2="))
c=int(input("Canh 3="))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if a==b==c:
        print("Tam giac deu")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("Tam giac can")
    else:
        print("Tam giac khac")
else:
    print("Khong hop le")
