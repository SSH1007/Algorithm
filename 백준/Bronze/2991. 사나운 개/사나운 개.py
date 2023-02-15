A, B, C, D = map(int, input().split())
PMN = list(map(int, input().split()))
for i in PMN:
    dap = 0
    if 0 < i%(A+B) <= A:
        dap+=1
    if 0 < i%(C+D) <= C:
        dap+=1
    print(dap)