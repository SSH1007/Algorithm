import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dr = [0, -1, -1, -1, 0, 1, 1, 1]
    dc = [-1, -1, 0, 1, 1, 1, 0, -1]

    N = int(input())
    mine = [list(input()) for _ in range(N)]
    touched = [list(input()) for _ in range(N)]
    dap = [['.']*N for _ in range(N)]

    tread = False
    for r in range(N):
        for c in range(N):
            if touched[r][c] == 'x':
                if mine[r][c] == '*':
                    tread = True
                else:
                    dap[r][c] = 0
                    for i in range(8):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if 0 <= nr < N and 0 <= nc < N:
                            if mine[nr][nc] == '*':
                                dap[r][c] += 1
    if tread:
        for r in range(N):
            for c in range(N):
                if mine[r][c] == '*':
                    dap[r][c] = '*'

    for d in dap:
        print(*d, sep='')


if __name__ == '__main__':
    main()