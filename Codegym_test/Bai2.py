#In ra so chia het cho 3 lon nhat trong mang
#Khai bao N
N = int(input("Input N: "))

# Kiem tra N > 0
while N <= 0:
    N = int(input("Input N > 0 : "))

# Khai bao Mang arr
arr = []
#Nhap Mang arr
for i in range(N):
    arr.append(int(input("Input arr[{}]: ".format(i))))

max_div_3 = None
# Kiem tra so chia het cho 3 lon nhat trong mang
for i in arr:
    if i % 3 == 0:
        if max_div_3 is None or i > max_div_3:
            max_div_3 = i
if max_div_3 is not None:
    print("So lon nhat chia het cho 3", max_div_3)
else:
    print("Khong co")
