n=float(input("So decibel="))
if n<40 or n>130:
    print("Tieng on khong nam trong bang")
elif n==40:
    print("Can phong im lang")
elif 40<n<70:
    print("Tieng on nam o giua can phong im lang va dong ho bao thuc")
elif n==70:
    print("Dong ho bao thuc")
elif 70<n<106:
    print("Tieng on nam o giua dong ho bao thuc va may cat co dung gas")
elif n==106:
    print("May cat co dung gas")
elif 106<n<130:
    print("Tieng on nam giua may cat co dung gas va bua khoan")
elif n==130:
    print("Bua khoan")
