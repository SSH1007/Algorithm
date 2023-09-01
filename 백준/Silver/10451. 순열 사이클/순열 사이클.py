def cycle(x):
    if visited[x]:
        return
    visited[x] = 1
    cycle(uplst[x])


import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    uplst = [0]*(N+1)
    lst = list(map(int, input().rstrip().split()))
    dap = 0
    for i in range(N):
        uplst[i+1] = lst[i]
    visited = [0]*(N+1)
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            cycle(uplst[i])
            dap += 1
    print(dap)