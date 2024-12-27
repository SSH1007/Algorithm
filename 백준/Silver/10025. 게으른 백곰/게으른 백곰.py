import sys
input = lambda: sys.stdin.readline().rstrip()


N, K = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
ice.sort(key=lambda x: x[1])
dap = 0
s, e, cur = 0, 0, 0
while s <= e and e < N:
    if ice[e][1]-ice[s][1] <= 2*K:
        cur += ice[e][0]
        dap = max(dap, cur)
        e += 1
    else:
        cur -= ice[s][0]
        s += 1
print(dap)