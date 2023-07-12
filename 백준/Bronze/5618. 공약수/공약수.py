def GCD(a, b):
    while b!=0:
        a, b = b, a%b
    return a

n = int(input())
lst = list(map(int, input().split()))
gcd = 0
for i in range(1, n):
    gcd = GCD(GCD(lst[i], lst[i-1]), gcd)
dap = set()
for i in range(1, int(gcd**0.5)+1):
    if gcd % i == 0:
        dap.add(i)
        dap.add(gcd//i)
dap = sorted(list(dap))
for d in dap:
    print(d)