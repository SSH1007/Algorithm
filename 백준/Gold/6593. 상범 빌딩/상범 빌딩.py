import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# 동서남북상하
dr = [0, 0, 1, -1, 0, 0]
dc = [1, -1, 0, 0, 0, 0]
dl = [0, 0, 0, 0, 1, -1]


def main():
    while 1:
        L, R, C = map(int, input().split())
        if L == R == C == 0:
            return
        building = []
        for _ in range(L):
            building.append([list(input()) for _ in range(R)])
            _ = input()

        end = []
        visited = [[[-1]*C for _ in range(R)] for _ in range(L)]
        q = deque()
        # 시작점, 끝점 체크
        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if building[l][r][c] == 'S':
                        q.append((l, r, c))
                        visited[l][r][c] = 0
                    elif building[l][r][c] == 'E':
                        end = [l, r, c]
        while q:
            z, y, x = q.popleft()
            for i in range(6):
                nz = z + dl[i]
                nr = y + dr[i]
                nc = x + dc[i]
                if 0 <= nz < L and 0 <= nr < R and 0 <= nc < C:
                    # 막혀있는 칸은 가지 않고
                    if building[nz][nr][nc] != '#':
                        # 아직 가지 않은 곳으로
                        if visited[nz][nr][nc] == -1:
                            visited[nz][nr][nc] = visited[z][y][x] + 1
                            q.append((nz, nr, nc))
       
        dap = visited[end[0]][end[1]][end[2]]
        if dap == -1:
            print('Trapped!')
        else:
            print('Escaped in %d minute(s).' % dap)


if __name__ == '__main__':
    main()