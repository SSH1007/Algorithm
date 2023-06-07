import sys
input = sys.stdin.readline
from collections import deque
N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

def bfs(start):
    global cnt
    que = deque([start])
    visited[start] = 1
    while que:
        n = que.popleft()
        for newNode in graph[n]:
            if visited[newNode]:
                continue
            cnt += 1
            visited[newNode] = cnt
            que.append(newNode)

bfs(R)
print(*visited[1:], sep='\n')