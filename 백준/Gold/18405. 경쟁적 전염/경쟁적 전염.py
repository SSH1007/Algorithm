import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(N)]
    S, X, Y = map(int, input().split())
    visited = [[0]*N for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    lst = []

    for i in range(N):
        for j in range(N):
            if info[i][j]:
                lst.append((info[i][j], i, j))
                visited[i][j] = info[i][j]
    lst.sort()
    q = deque(lst)
    nq = deque()

    def BFS(q):
        # print(q)
        while q:
            num, r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if not visited[nr][nc]:
                        visited[nr][nc] = num
                        nq.append((num, nr, nc))
        # print(q)
        q.extend(nq)
        nq.clear()
        # print(q)

    for _ in range(S):
        BFS(q)

        # for v in visited:
        #     print(v)
    print(visited[X-1][Y-1])


if __name__ == '__main__':
    main()