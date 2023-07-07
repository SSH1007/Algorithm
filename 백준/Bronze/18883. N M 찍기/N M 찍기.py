N, M = map(int, input().split())
dap = 0
for _ in range(N):
    lst = []
    for _ in range(M):
        dap+=1
        lst.append(dap)
    print(*lst)