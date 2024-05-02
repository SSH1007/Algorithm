import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().rstrip().split())
graph = [[]*(N+1) for _ in range(N+1)]
for _ in range(K):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    graph[B].append(A)
dap = True


def BFS(start, cnt):
    visited = [0]*(N+1)
    q = deque([(start, cnt)])
    visited[start] = 1
    while q:
        s, c = q.popleft()
        if c > 6:
            return False
        for node in graph[s]:
            if not visited[node]:
                visited[node] = 1
                q.append((node, c+1))
    if sum(visited) != N:
        return False
    return True


# 모든 사람이 연결이 되지 않거나, 연결이 되어도 6단계를 초과하면 Big World!
for n in range(1, N+1):
    dap = BFS(n, 0)
if dap:
    print('Small World!')
else:
    print('Big World!')