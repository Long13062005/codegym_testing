#In ra so nguyen to nho hon N
# Khai bao N
N = int(input("Input N: "))

# Kiem tra N > 0
while N <= 0:
    N = int(input("Input N > 0 : "))

# Kiem tra N <= 2
if N <= 2:
    print("Khong co so nguyen to")

# Kiem tra so nguyen to
for i in range(2, N):
    isPrime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
