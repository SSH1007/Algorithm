import sys
input = sys.stdin.readline
from collections import deque
R, C = map(int, input().rstrip().split())
yard = [list(input().rstrip()) for _ in range(R)]
# 델타 탐색으로 각 영역 안 양과 늑대 수 세기
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
sheep_wolf = []
visited = [[0]*C for _ in range(R)]
for yr in range(R):
    for yc in range(C):
        # 울타리면 pass
        if yard[yr][yc] == '#':
            continue
        sheep, wolf = 0, 0
        # 1칸 짜리에서도 양 늑대 판별
        if not visited[yr][yc]:
            if yard[yr][yc] == 'v':
                wolf += 1
            elif yard[yr][yc] == 'o':
                sheep += 1
        # 2칸 이상의 영역이라면 큐 동작
        q = deque([(yr, yc)])
        while q:
            r, c = q.popleft()
            visited[r][c] = 1
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc] and yard[nr][nc] != '#':
                        visited[nr][nc] = 1
                        if yard[nr][nc] == 'v':
                            wolf += 1
                        elif yard[nr][nc] == 'o':
                            sheep += 1
                        q.append((nr, nc))
        if sheep == 0 and wolf == 0:
            continue
        sheep_wolf.append((sheep, wolf))


ds, dw = 0, 0
for s, w in sheep_wolf:
    if s > w:
        ds += s
    else:
        dw += w
print(ds, dw)