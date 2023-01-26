def W(n):
    dap = 0
    for k in range(1,n+1):
        dap+=(k*(k+1)*(k+2)//2)
    return dap

T = int(input())
for _ in range(T):
    n = int(input())
    dap = W(n)
    print(dap)