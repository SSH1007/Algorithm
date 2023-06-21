import sys
input = sys.stdin.readline
N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

from collections import deque
def bfs(r):
    cnt = 1
    visited[r] = 1
    q = deque([(r)])
    while q:
        u = q.popleft()
        for node in sorted(graph[u], reverse=True):
            if visited[node] == 0:
                cnt += 1
                visited[node] = cnt
                q.append(node)
bfs(R)

for v in visited[1:]:
    print(v)