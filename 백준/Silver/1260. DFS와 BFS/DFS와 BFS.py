def DFS(V):
    visited1[V] = 1
    print(V, end=' ')
    nodes[V].sort()
    for v in nodes[V]:
        if not visited1[v]:
            DFS(v)

from collections import deque
def BFS(V):
    que = deque([V])
    visited2[V] = 1
    while que:
        S = que.popleft()
        print(S, end=' ')
        for s in nodes[S]:
            if not visited2[s]:
                visited2[s] = 1
                que.append(s)
                
N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
visited1 = [0 for _ in range(N+1)]
visited2 = [0 for _ in range(N+1)]
for m in range(M):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
DFS(V)
print()
BFS(V)