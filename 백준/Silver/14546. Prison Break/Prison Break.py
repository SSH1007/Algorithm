import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
P = int(input())
for _ in range(P):
    L, W, A, B, C, D = map(int, input().split())
    A, B, C, D = A-1, W-B, C-1, W-D
    maps = [list(input()) for _ in range(W)]
    visited = [[0]*L for _ in range(W)]
    q = deque([(B, A)])
    visited[B][A] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < W and 0 <= nc < L:
                if not visited[nr][nc] and maps[nr][nc] == maps[r][c]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
                
    if visited[D][C]:
        print('YES')
    else:
        print('NO')