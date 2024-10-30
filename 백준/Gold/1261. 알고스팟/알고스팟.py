# 0-1 BFS : 1261 알고스팟
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def main():
    M, N = map(int, input().split())
    maps = [list(input()) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == -1:
                    if maps[nr][nc] == '0':
                        q.appendleft((nr, nc))
                        visited[nr][nc] = visited[r][c]
                    else:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[r][c] + 1
    print(visited[N-1][M-1])


if __name__ == '__main__':
    main()