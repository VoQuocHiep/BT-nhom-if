t=int(input("Tuoi nguoi="))
if 0<t<=2:
    tc=10.5*t
    print(tc)
elif t>2:
    tc=10.5*2+(t-2)*4
    print(tc)
else:
    print("Khong thich hop")
