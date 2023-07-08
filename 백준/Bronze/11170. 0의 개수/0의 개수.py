T = int(input())
for _ in range(T):
    dap = 0
    a, b = map(int, input().split())
    for i in range(a, b+1):
        dap+=str(i).count('0')
    print(dap)