def Fib(n):
    if n<=1:
        return n
    return Fib(n-1) + Fib(n-2)

n = int(input())
f0 = 0
f1 = 1
if n<=1:
    print(n)
else:
    while 1:
        if n<=1:
            break
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        n-=1
    print(f2)