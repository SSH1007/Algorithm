import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(N+1)]

def dfs(start):
    visited[start] = 1
    for newNode in graph[start]:
        if not visited[newNode]:
            dfs(newNode)

tmp = 0
cnt = 0
for i in range(1,N+1):
    dfs(i)
    if tmp != sum(visited):
        cnt+=1
        tmp = sum(visited)
print(cnt)