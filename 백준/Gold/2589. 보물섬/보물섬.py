import sys
input = sys.stdin.readline
from collections import deque


def main():
    # 각 육지에서 BFS로 도달할 수 있는 최단 거리들 중 최댓값을 구하는 문제
    R, C = map(int, input().rstrip().split())
    # L = land, W = water
    maps = [list(input().rstrip()) for _ in range(R)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]


    def BFS(r, c):
        q = deque([(r, c)])
        visited[r][c] = 1
        while q:
            cr, cc = q.popleft()
            for i in range(4):
                nr = cr + dr[i]
                nc = cc + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc] and maps[nr][nc] == 'L':
                        q.append((nr, nc))
                        visited[nr][nc] = visited[cr][cc]+1
        dap = 0
        for v in visited:
            dap = max(dap, max(v))
        return dap


    dap = 0
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'L':
                visited = [[0]*C for _ in range(R)]
                dap = max(dap, BFS(r, c))
    print(dap-1)


if __name__ == '__main__':
    main()