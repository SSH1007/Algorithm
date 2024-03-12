import sys
input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
farm = [list(input().rstrip()) for _ in range(R)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]


def setFence():
    for r in range(R):
        for c in range(C):
            if farm[r][c] == 'W':
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        if farm[nr][nc] == 'S':
                            return False
                        if farm[nr][nc] == '.':
                            farm[nr][nc] = 'D'
    return True


dap = setFence()
if dap:
    print(1)
    for f in farm:
        print(*f, sep='')
else:
    print(0)