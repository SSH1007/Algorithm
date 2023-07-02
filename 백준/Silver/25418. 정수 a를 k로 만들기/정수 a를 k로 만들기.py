import sys
input = sys.stdin.readline

from collections import deque
A, K = map(int, input().rstrip().split())
graph = [[] for _ in range(K+1)]
visited = [0]*(K+1)
dap = 0

q = deque([A])
while q:
    x = q.popleft()
    if x == K:
        break
    for node in [x+1, x*2]:
        if node <= K and not visited[node]:
            q.append(node)
            visited[node] = visited[x]+1

print(visited[K])