not_nhac = input("Nhap not nhac: ")
note = not_nhac[0]
n = int(not_nhac[1])
tan_so = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88
}
if note == "C" and 0 <= n <= 8:
    freq = tan_so["C4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "D" and 0 <= n <= 8:
    freq = tan_so["D4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "E" and 0 <= n <= 8:
    freq = tan_so["E4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "F" and 0 <= n <= 8:
    freq = tan_so["F4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "G" and 0 <= n <= 8:
    freq = tan_so["G4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "A" and 0 <= n <= 8:
    freq = tan_so["A4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
elif note == "B" and 0 <= n <= 8:
    freq = tan_so["B4"] / 2 ** (4 - n)
    print("Not nhac", not_nhac, "co tan so la", freq, "Hz")
else:
    print("Not nhac khong hop le!")
