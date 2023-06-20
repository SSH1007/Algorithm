import sys
input = sys.stdin.readline
from collections import deque
# 입력
N, M = map(int, input().rstrip().split())
graph = [input().rstrip() for _ in range(N)]
# 기타 변수 정의
visited = [[0]*(M) for _ in range(N)]
dap = 0
# bfs 정의
def bfs(r,c):
    global dap
    q = deque([(r,c)])
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                if graph[nr][nc] == 'P':
                    dap += 1
                if graph[nr][nc] != 'X':
                    q.append((nr, nc))
                    visited[nr][nc] = 1
# bfs 동작
for n in range(N):
    for m in range(M):
        if graph[n][m] == 'I':
            bfs(n, m)
print(dap if dap else 'TT')