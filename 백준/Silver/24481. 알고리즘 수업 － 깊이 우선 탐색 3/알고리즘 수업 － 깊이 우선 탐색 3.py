import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()


def DFS(s):
    for next in graph[s]:
        if visited[next] == -1:
            visited[next] = visited[s]+1
            DFS(next)


visited[R] = 0
DFS(R)
for i in range(1, N+1):
    print(visited[i])