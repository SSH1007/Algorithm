T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    dap = 0
    for _ in range(N):
        vi, fi, ci = map(int, input().split())
        if vi*(fi/ci) >= D:
            dap += 1
    print(dap)