import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def main():
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    def BFS(r, c, cn):
        q = deque([(r, c)])
        visited[r][c] = cn
        flag = True
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if visited[nr][nc] == -1:
                        if maps[nr][nc] == maps[r][c]:
                            q.append((nr, nc))
                            visited[nr][nc] = cn
                    if maps[nr][nc] > maps[r][c]:
                        flag = False
        if flag:
            return 1
        else:
            return 0

    dap = 0
    for n in range(N):
        for m in range(M):
            if visited[n][m] == -1:
                dap += BFS(n, m, maps[n][m])
    print(dap)


if __name__ == '__main__':
    main()