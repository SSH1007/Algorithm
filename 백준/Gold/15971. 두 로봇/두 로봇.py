import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, A, B = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    s, e, d = map(int, input().split())
    graph[s].append((e, d))
    graph[e].append((s, d))

q = deque([(A, 0, 0)])
visited = [0]*(N+1)
visited[A] = 1


def BFS():
    while q:
        cur, total, max_v = q.popleft()
        if cur == B:
            return total-max_v
        for next, dist in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                q.append((next, total+dist, max(dist, max_v)))


print(BFS())