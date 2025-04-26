#Fibonacci bang de quy, in ra day tu f(1) den f(n) , kiem tra n <= 30
# # # Khai bao N
N = int(input("Input N: "))

# # # Kiem tra N > 0
while N <= 0 :
    N = int(input("Input N > 0 : "))
while N > 30:
    print("Khong co so Fibonacci")
    N = int(input("Input N <= 30 : "))
# # # Ham de quy tinh so Fibonacci
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Dung memoization/array de toi uu
# # # Ham de quy tinh so Fibonacci voi memoization
memo = {}
def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        return memo[n]

# # # Kiem tra N <= 30
if N > 30:
    print("Khong co so Fibonacci")
else:
    # # # In ra day Fibonacci tu f(1) den f(n)
    for i in range(1, N + 1):
        print(fibonacci_memo(i), end=" ")
    print()
    for i in range(1, N + 1):
        print(fibonacci(i), end=" ")

#cho thay memo se nhanh hon binh thuong


