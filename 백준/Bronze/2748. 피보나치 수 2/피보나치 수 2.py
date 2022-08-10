# 시간 초과 때문에 재귀가 아니라 반복문으로 풀이
def fibo(n): # n 범위가 자연수이므로 n<=2만 신경쓰면 됨
    fib = [1,1]
    if n <= 2:
        return 1
    else:
        for i in range(3,n):
            temp = fib[0]+fib[1]
            fib[0] = fib[1]
            fib[1] = temp
        return (fib[0]+fib[1])

n = int(input())
print(fibo(n))