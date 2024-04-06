import sys
input = sys.stdin.readline
N = int(input().rstrip())
garden = [list(map(int, input().rstrip().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dap = 200*100


def F(lst):
    value = 0
    s = set()
    for l in lst:
        r = l//N
        c = l % N
        tmp = garden[r][c]
        s.add((r, c))
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                return 200*100
            tmp += garden[nr][nc]
            s.add((nr, nc))
        value += tmp
    if len(s) != 15:
        return 200*100
    return value


for i in range(N+1, N*N):
    for j in range(i+1, N*N):
        for k in range(j+1, N*N):
            dap = min(dap, F((i, j, k)))
print(dap)