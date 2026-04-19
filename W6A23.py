def delete(mang, x):
    mang2 = []
    for i in mang:
        if i>= x:
            mang2.append(i)
    return mang2
mang = list(map(int, input("nhap so phan tu cua mang: ").split()))
x = int(input("nhap phan tu can xoa: "))
print("mang vua nhap la: ", mang)
print("mang sau khi xoa la: ", delete(mang, x))