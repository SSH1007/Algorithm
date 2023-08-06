K = int(input())
for _ in range(K):
    dap = 0
    P, M = map(int, input().split())
    lst = [0]*(M+1)
    for _ in range(P):
        n = int(input())
        if not lst[n]:
            lst[n] = 1
        else:
            dap +=1
    print(dap)