def F(n):
    r = n
    i = 2
    while i<=n:
        r+=(n//i)*(i//2)
        i*=2
    return r

a, b = map(int, input().split())
print(F(b)-F(a-1))