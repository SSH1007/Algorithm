import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def DFS(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc]:
                if L <= abs(maps[nr][nc]-maps[r][c]) <= R:
                    visited[nr][nc] = group
                    DFS(nr, nc)


N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dap = 0
while 1:
    # 국경선을 공유하는 두 나라간 인구차가 L~R인지 확인하여 연합 구성
    visited = [[0]*N for _ in range(N)]
    group = 1
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = group
                DFS(r, c)
                group += 1

    dic = {i: [] for i in range(1, group)}
    for r in range(N):
        for c in range(N):
            dic[visited[r][c]].append((r, c))
    # 연합 인구수 파악
    for i in range(1, group):
        total, cnt = 0, 0
        for r, c in dic[i]:
            total += maps[r][c]
            cnt += 1
        newP = total//cnt
    # 인구수 maps 재구성
        for r, c in dic[i]:
            maps[r][c] = newP

    dap += 1

    if len(dic) == N**2:
        break
print(dap-1)