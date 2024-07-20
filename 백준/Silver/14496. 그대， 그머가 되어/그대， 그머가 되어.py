import sys
input = lambda:sys.stdin.readline().rstrip()
from collections import deque


def main():
    A, B = map(int, input().split())
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    visited = [-1]*(N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)

    q = deque()
    q.append(A)
    visited[A] = 0
    while q:
        p = q.popleft()
        for node in lst[p]:
            if visited[node] == -1:
                q.append(node)
                visited[node] = visited[p]+1

    print(visited[B])


if __name__ == '__main__':
    main()