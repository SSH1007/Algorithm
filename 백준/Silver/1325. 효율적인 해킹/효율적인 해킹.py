import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().rstrip().split())
lst = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().rstrip().split())
    lst[B].append(A)


def BFS(l):
    visited = [0]*(N+1)
    q = deque([l])
    visited[l] = 1
    cnt = 0
    while q:
        s = q.popleft()
        for new_node in lst[s]:
            if not visited[new_node]:
                q.append(new_node)
                visited[new_node] = 1
                cnt += 1

    return cnt


tmp_dap = []
for i in range(1, N+1):
    tmp_dap.append((i, BFS(i)))
maxv = sorted(tmp_dap, key=lambda x:-x[1])[0][1]
dap = []
for t in tmp_dap:
    if t[1] == maxv:
        dap.append(t[0])
print(*sorted(dap))