import sys
input = sys.stdin.readline

def fibo(n):
    a, b = 1, 1
    for _ in range(n-2):
        a, b = b, a+b
    return b

def dp(n):
    return n-2

n = int(input().rstrip())
print(fibo(n), dp(n))