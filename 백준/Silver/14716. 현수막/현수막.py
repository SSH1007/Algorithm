import sys
input = sys.stdin.readline
from collections import deque


def main():
    M, N = map(int, input().rstrip().split())
    # 상하좌우 상\ 상/ 하\ 하/
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, -1, 1, 1, -1]
    mak = [list(map(int, input().rstrip().split())) for _ in range(M)]
    visited = [[0]*N for _ in range(M)]
    dap = 0


    def BFS(m, n):
        q = deque()
        q.append((m, n))
        visited[m][n] = 1
        while q:
            r, c = q.popleft()
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < M and 0 <= nc < N:
                    if mak[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
        return 1


    for m in range(M):
        for n in range(N):
            if mak[m][n] == 1 and not visited[m][n]:
                dap += BFS(m, n)
    print(dap)


if __name__ == '__main__':
    main()