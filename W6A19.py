def maxindex(n):
    max_value = max(n)
    max_index = n.index(max_value)
    return max_index
n = list(map(int, input("nhap so phan tu cua mang: ").split()))
print("mang vua nhap la: ", n)
print("vi tri cua phan tu lon nhat la: ", maxindex(n))
