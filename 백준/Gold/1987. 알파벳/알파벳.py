import sys
input = lambda: sys.stdin.readline().rstrip()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

R, C = map(int, input().split())
dap = 0
maps = [list(input()) for _ in range(R)]
s = set()
s.add(maps[0][0])


def DFS(r, c, cnt):
    global dap
    dap = max(dap, cnt)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not maps[nr][nc] in s:
                s.add(maps[nr][nc])
                DFS(nr, nc, cnt+1)
                s.remove(maps[nr][nc])


DFS(0, 0, 1)
print(dap)