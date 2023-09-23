N = int(input())
for _ in range(N):
    M = int(input())
    dap = 0
    lst = []
    for _ in range(M):
        K, D, A = map(int, input().split())
        lst.append((K, D, A))
    k, d, a = map(int, input().split())
    for l in lst:
        if l[0]*k - l[1]*d + l[2]*a > 0:
            dap += (l[0]*k - l[1]*d + l[2]*a)
    print(dap)