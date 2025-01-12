import sys
input = lambda: sys.stdin.readline().rstrip()


def DFS(node):
    for next in As[node]:
        if not visited[next]:
            visited[next] = visited[node]+1
            DFS(next)


T = int(input())
for _ in range(T):
    N = int(input())
    As = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        A = int(input())
        As[i].append(A)
    visited = [0]*(N+1)
    DFS(1)
    print(visited[N])