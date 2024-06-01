R, C, K = map(int, input().split())
Map = [list(input()) for _ in range(R)]
dap = 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def DFS(r, c, l):
    global dap
    if r == 0 and c == C-1 and l == K:
        dap += 1
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if Map[nr][nc] != 'T':
                Map[r][c] = 'T'
                DFS(nr, nc, l+1)
                Map[r][c] = '.'


DFS(R-1, 0, 1)
print(dap)