from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
yard = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
d1, d2 = 0, 0


def BFS(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    # 양 k, 늑대 v
    k, v = 0, 0
    while q:
        sr, sc = q.popleft()
        if yard[sr][sc] == 'k':
            k += 1
        elif yard[sr][sc] == 'v':
            v += 1
        for i in range(4):
            nr = dr[i] + sr
            nc = dc[i] + sc
            if 0 <= nr < R and 0 <= nc < C:
                if not visited[nr][nc] and yard[nr][nc] != '#':
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    if v >= k:
        k = 0
    else:
        v = 0
    return [k, v]


for r in range(R):
    for c in range(C):
        if yard[r][c] != '#' and not visited[r][c]:
            v, k = BFS(r, c)
            d1 += v
            d2 += k

print(d1, d2)