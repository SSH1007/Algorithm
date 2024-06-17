import sys
input = sys.stdin.readline
from collections import deque


def main():
    N, M = map(int, input().rstrip().split())
    visited = [-1]*(N+1)
    lst = [[] for _ in range(N+1)]
    for _ in range(M):
        A_i, B_i = map(int, input().rstrip().split())
        lst[A_i].append(B_i)
        lst[B_i].append(A_i)
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        start = q.popleft()
        for node in lst[start]:
            if visited[node] == -1:
                q.append(node)
                visited[node] = visited[start]+1
    maxDis = max(visited)
    print(visited.index(maxDis), maxDis, visited.count(maxDis))


if __name__ == '__main__':
    main()