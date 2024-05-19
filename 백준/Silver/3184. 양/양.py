import sys
input = sys.stdin.readline
from collections import deque
R, C = map(int, input().rstrip().split())
yard = [list(input().rstrip()) for _ in range(R)]
# 델타 탐색으로 각 영역 안 양과 늑대 수 세기
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dap_s, dap_w = 0, 0
visited = [[0]*C for _ in range(R)]
for yr in range(R):
    for yc in range(C):
        if yard[yr][yc] == 'v' and not visited[yr][yc] or \
            yard[yr][yc] == 'o' and not visited[yr][yc]:
            sheep, wolf = 0, 0
            q = deque([(yr, yc)])
            while q:
                r, c = q.popleft()
                if not visited[r][c]:
                    visited[r][c] = 1
                    if yard[r][c] == 'v':
                        wolf += 1
                    elif yard[r][c] == 'o':
                        sheep += 1
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < R and 0 <= nc < C:
                            if not visited[nr][nc] and yard[nr][nc] != '#':
                                q.append((nr, nc))
            if sheep > wolf:
                dap_s += sheep
            else:
                dap_w += wolf
print(dap_s, dap_w)