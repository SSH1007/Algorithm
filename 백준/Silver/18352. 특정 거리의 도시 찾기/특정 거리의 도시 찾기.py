import sys
input = sys.stdin.readline
from collections import deque
N, M, K, X = map(int, input().rstrip().split())
info = [[] for _ in range(N+1)]
dist = [-1 for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    info[A].append(B)


def BFS(start):
    q = deque([start])
    dist[start] = 0
    while q:
        next = q.popleft()
        for node in info[next]:
            if dist[node] == -1:
                dist[node] = dist[next] + 1
                q.append(node)
    return


BFS(X)
lst = []
for i in range(N+1):
    if dist[i] == K:
        lst.append(i)
if lst:
    print(*lst, sep='\n')
else:
    print(-1)