import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    N, M = map(int, input().split())
    inf = float('inf')
    maps = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[[inf]*M for _ in range(N)] for _ in range(2)]
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    visited[1][0][0] = 1

    while q:
        r, c, dim = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[dim][nr][nc] == inf:
                    if maps[nr][nc] == 0:
                        q.append((nr, nc, dim))
                        visited[dim][nr][nc] = min(visited[dim][nr][nc], visited[dim][r][c] + 1)
                    else:
                        if dim == 0:
                            q.append((nr, nc, dim+1))
                            visited[dim+1][nr][nc] = min(visited[dim+1][nr][nc], visited[dim][r][c] + 1)
    if visited[1][N-1][M-1] == visited[0][N-1][M-1] == inf:
        print(-1)
    else:
        print(min(visited[1][N-1][M-1], visited[0][N-1][M-1]))


if __name__ == '__main__':
    main()