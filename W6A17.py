n = int(input("nhap kich thuoc cua ma tran vuong: "))

ma_tran = []

print("nhap cac phan tu cua ma tran nxn :")
for i in range(n):
    hang = list(map(int, input(f"hang {i+1}: ").split()))
    ma_tran.append(hang)

print("ma tran vua nhap la:")
for i in range(n):
    for j in range(n):
        print(f"{ma_tran[i][j]:>4}", end="")
    print()
cheochinh = []
cheophu = []
for i in range(n):
    cheochinh.append(ma_tran[i][i])
    cheophu.append(ma_tran[i][n-1-i])
print("cheo chinh la: ", cheochinh)
print("cheo phu la: ", cheophu)