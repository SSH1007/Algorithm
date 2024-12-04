import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


N, M = map(int, input().split())
S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited[S] = 1
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def BFS():
    q = deque([(S, 0)])
    while q:
        now, sec = q.popleft()
        if now == E:
            print(sec)
            break
        for i in [-1, 1]:
            if 1 <= now+i <= N and not visited[now+i]:
                visited[now+i] = 1
                q.append((now+i, sec+1))
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, sec+1))


BFS()