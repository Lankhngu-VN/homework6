def finder(list, k):
    for i in range(len(list)):
        if list[i] == k:
            return i
    return -1
n = list(map(int, input("nhap so phan tu cua mang: ").split()))
k = int(input("nhap phan tu can tim: "))
print(finder(n, k))