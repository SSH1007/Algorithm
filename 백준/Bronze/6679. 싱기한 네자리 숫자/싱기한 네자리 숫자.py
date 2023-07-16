def base(n, m):
    dap = 0
    while n!=0:
        dap += n%m
        n//=m
    return dap

for i in range(1000, 10000):
    if base(i,10) == base(i, 12) == base(i, 16):
        print(i)