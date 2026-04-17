n= int(input("nhap so hang cua ma tran: "))
m= int(input("nhap so cot cua ma tran: "))

ma_tran = []

print("nhap cac phan tu cua ma tran ( nhap tung hang cach nhau boi dau cach):")
for i in range(n):
    hang = list(map(int, input(f"Hàng {i+1}: ").split()))
    ma_tran.append(hang)
print("ma tran vua nhap la:")
for i in range(n):
    for j in range(m):
        print(f"{ma_tran[i][j]:>4}", end="")
    print()