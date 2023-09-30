N = int(input())
for _ in range(N):
    a = int(input())
    dap = 0
    for i in range(a):
        dap += (i+1)**2
    print(dap)