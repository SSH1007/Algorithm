import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().rstrip().split())
graph = [input().rstrip() for _ in range(R)]
visited = [[False] * C for _ in range(R)]
dap = 0

def bfs(r,c):
    q = deque([(r,c)])
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()
        for dr, dc in [(1,0), (0,1)]:
            nr = cr+dr
            nc = cc+dc
            if 0<=nr<R and 0<=nc<C and not visited[nr][nc]:
                if graph[nr][nc] == '#':
                    q.append((nr, nc))
                    visited[nr][nc] = True

for r in range(R):
    for c in range(C):
        if not visited[r][c] and graph[r][c] == '#':
            bfs(r,c)
            dap+=1

print(dap)