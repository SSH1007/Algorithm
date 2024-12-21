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
visited[R] = 0
for g in graph:
    g.sort(reverse=True)


def DFS(now):
    for next in graph[now]:
        if visited[next] == -1:
            visited[next] = visited[now] + 1
            DFS(next)


DFS(R)
for i in range(1, N+1):
    print(visited[i])