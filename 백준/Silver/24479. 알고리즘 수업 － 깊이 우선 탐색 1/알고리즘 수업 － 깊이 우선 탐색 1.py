import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
# 무방향 그래프 = 양방향 그래프
for _ in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# 정점번호는 오름차순으로 방문
for g in graph:
    g.sort()

def dfs(start):
    global cnt
    visited[start] = cnt
    # print(visited, cnt)
    cnt += 1
    for node in graph[start]:
        if visited[node] == 0:
            dfs(node)

dfs(R)

for i in visited[1:]:
    print(i)