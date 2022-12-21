n = int(input())
fib = [1,1,1] + [0 for _ in range(n)]
for i in range(3,n):
    fib[i] = fib[i-1]+fib[i-3]
print(fib[n-1])