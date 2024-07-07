import sys
input = sys.stdin.readline
from collections import deque
# 노드의 개수 N, 거리를 알고 싶은 노드쌍의 개수 M
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    # 연결된 a점과 b점 사이의 거리는 l
    a, b, l = map(int, input().rstrip().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def BFS(start, end, dist):
    q = deque([(start, dist)])
    visited[start] = 1

    while q:
        point, d = q.popleft()
        if point == end:
            return d
        for node, length in graph[point]:
            if not visited[node]:
                q.append((node, d+length))
                visited[node] = 1


for _ in range(M):
    # a점과 b점 사이의 거리를 알고 싶다!
    a, b = map(int, input().rstrip().split())
    visited = [0]*(N+1)
    print(BFS(a, b, 0))