import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


def DFS(start, flag):
    for node in lst[start]:
        if not visited[node]:
            visited[node] = flag*-1
            result = DFS(node, flag*-1)
            if not result:
                return False
        else:
            if flag == visited[node]:
                return False
    return True


K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    lst = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        lst[u].append(v)
        lst[v].append(u)

    visited = [0]*(V+1)
    for v in range(1, V+1):
        if not visited[v]:
            visited[v] = 1
            result = DFS(v, 1)
            if not result:
                break
    print('YES' if result else 'NO')