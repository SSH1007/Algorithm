import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

q = deque()
q.append(R)
visited[R] = 0
while q:
    cur = q.popleft()
    for next in graph[cur]:
        if visited[next] == -1:
            visited[next] = visited[cur] + 1
            q.append(next)
for i in range(1, N+1):
    print(visited[i])