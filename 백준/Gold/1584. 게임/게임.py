import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    maps = [[0]*501 for _ in range(501)]

    N = int(input())
    for _ in range(N):
        X1, Y1, X2, Y2 = map(int, input().split())
        for r in range(min(Y1, Y2), max(Y1, Y2)+1):
            for c in range(min(X1, X2), max(X1, X2)+1):
                maps[r][c] = 1

    M = int(input())
    for _ in range(M):
        X1, Y1, X2, Y2 = map(int, input().split())
        for r in range(min(Y1, Y2), max(Y1, Y2)+1):
            for c in range(min(X1, X2), max(X1, X2)+1):
                maps[r][c] = 2

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    maps[0][0] = 0
    visited = [[-1]*501 for _ in range(501)]
    visited[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 501 and 0 <= nc < 501:
                if visited[nr][nc] == -1:
                    if maps[nr][nc] == 0:
                        q.appendleft((nr, nc))
                        visited[nr][nc] = visited[r][c]
                    elif maps[nr][nc] == 1:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1

    print(visited[500][500])


if __name__ == '__main__':
    main()