import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = [list(input().rstrip()) for _ in range(N)]
dap = [[0]*N for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if a == b:
                continue
            if lst[a][b] == 'Y' or (lst[a][k] == 'Y' and lst[k][b] == 'Y'):
                dap[a][b] = 1

ans = 0
for d in dap:
    ans = max(ans, sum(d))
print(ans)