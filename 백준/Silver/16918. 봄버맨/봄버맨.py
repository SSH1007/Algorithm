import sys
input = sys.stdin.readline
R, C, N = map(int, input().rstrip().split())
pan = [list(input().rstrip()) for _ in range(R)]
bomb = [[0]*C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for r in range(R):
    for c in range(C):
        if pan[r][c] == '.':
            bomb[r][c] = 0
        else:
            bomb[r][c] = 2

for _ in range(N-1):
    visited = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if bomb[r][c] == 3:
                bomb[r][c] = 0
                for i in range(4):
                    nr = r+dr[i]
                    nc = c+dc[i]
                    if 0 <= nr < R and 0 <= nc < C and bomb[nr][nc] != 3:
                        bomb[nr][nc] = 0
                        visited[nr][nc] = 1
            else:
                if not visited[r][c]:
                    bomb[r][c] += 1


for r in range(R):
    for c in range(C):
        if bomb[r][c] == 0:
            print('.', end='')
        else:
            print('O', end='')
    print()