n=input("Thang: ")
if n in ["1","3","5","7","8","10","12"]:
    print("Thang",n,"co 31 ngay")
elif n in ["4","6","9","11"]:
    print("Thang",n,"co 30 ngay")
elif n=="2":
    print("Thang",n, "co 28 hoac 29 ngay")
else:
    print("thang",n,"khong ton tai")
    
