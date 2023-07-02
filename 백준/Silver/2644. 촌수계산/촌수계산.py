import sys
input = sys.stdin.readline

from collections import deque
n = int(input().rstrip())
start, end = map(int, input().rstrip().split())
m = int(input().rstrip())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
dap = 0

for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

q = deque([start])
while q:
    x = q.popleft()
    if x == end:
        break
    for node in graph[x]:
        if not visited[node]:
            q.append(node)
            visited[node] = visited[x]+1

if visited[end]:
    print(visited[end])
else:
    print(-1)