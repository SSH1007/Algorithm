from collections import deque
def bfs(start):
    visited = [0]*(N+1)
    visited[start] = 1
    q = deque([start])
    while q:
        v = q.popleft()
        for newNode in graph[v]:
            if not visited[newNode]: 
                visited[newNode] = visited[v] + 1
                q.append(newNode)
    return sum(visited)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

dap = []
for i in range(1, N+1):
    dap.append(bfs(i))
print(dap.index(min(dap))+1)