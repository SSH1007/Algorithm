from itertools import combinations
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
zlst = list(map(list, zip(*lst)))

dap = 0
for a, b, c in combinations(zlst, 3):
    tmp = 0
    for i in range(N):
        tmp += max(a[i], b[i], c[i])
    dap = max(dap, tmp)
print(dap)