#Dem gia so luong phan biet
# # Khai bao N
N = int(input("Input N: "))

# Kiem tra N > 0
while N <= 0:
    N = int(input("Input N > 0 : "))

# Khai bao Mang arr
arr = []
# Nhap Mang arr
for i in range(N):
    arr.append(input("Input arr[{}]: ".format(i)))
# Khai bao set de luu cac gia tri phan biet
unique_values = set(arr)
# Dem so luong gia tri phan biet
count_unique = len(unique_values)
print("So luong gia tri phan biet trong mang:", count_unique)
