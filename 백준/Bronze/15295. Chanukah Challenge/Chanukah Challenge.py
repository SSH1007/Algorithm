P = int(input())
for _ in range(P):
    K, N = map(int, input().split())
    dap = 0
    for n in range(1, N+1):
        dap += n
    print(K, dap+N)