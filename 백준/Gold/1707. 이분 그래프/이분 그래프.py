import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def BFS(visited, v, lst):
    q = deque([(v, 1)])
    visited[v] = 1
    while q:
        cur, group = q.popleft()
        for node in lst[cur]:
            if not visited[node]:
                visited[node] = group*-1
                q.append((node, group*-1))
            else:
                if visited[node] == group:
                    return False
    return True


def main():
    K = int(input())
    for _ in range(K):
        V, E = map(int, input().split())
        lst = [[] for _ in range(V+1)]
        for _ in range(E):
            u, v = map(int, input().split())
            lst[u].append(v)
            lst[v].append(u)
        result = True
        visited = [0]*(V+1)
        for v in range(1, V+1):
            if not visited[v]:
                result = BFS(visited, v, lst)
                if not result:
                    break
        print('YES' if result else 'NO')


if __name__ == '__main__':
    main()