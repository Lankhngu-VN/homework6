chuoi = input("nhap chuoi: ")
tu = chuoi.split()
tudien = {}
for i, tu in enumerate(tu):
    if tu not in tudien:
        tudien[tu] = ()
    tudien[tu] += (i,)
print(tudien)
