pan = [list(input().split()) for _ in range(5)]
dap = 0
visited = [0]*1000000
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def DFS(r, c, num):
    global dap
    if len(num) == 6 and not visited[int(num)]:
        visited[int(num)] = 1
        dap += 1
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 5 and 0 <= nc < 5:
                if len(num) < 6:
                    DFS(nr, nc, num+pan[nr][nc])


for i in range(5):
    for j in range(5):
        DFS(i, j, '')
print(dap)