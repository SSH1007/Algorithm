import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
lst = [list(input().rstrip()) for _ in range(N)]


def BFS(root, cnt):
    q = deque([(root, cnt)])
    visited[root] = 1
    while q:
        r, c = q.popleft()
        # 둘의 사이가 2 이상이라면 패스
        if c >= 2:
            continue
        for n in range(N):
            if not visited[n] and lst[r][n] == 'Y':
                visited[n] = 1
                q.append((n, c+1))


dap = 0
for n in range(N):
    visited = [0]*N
    BFS(n, 0)
    dap = max(dap, sum(visited)-1)
print(dap)