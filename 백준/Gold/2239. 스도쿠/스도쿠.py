import sys
input = lambda: sys.stdin.readline().rstrip()


def garo(r, num):
    for n in range(9):
        if maps[r][n] == num:
            return False
    return True


def sero(c, num):
    for n in range(9):
        if maps[n][c] == num:
            return False
    return True


def nine(r, c, num):
    nr, nc = (r//3)*3, (c//3)*3
    for n in range(nr, nr+3):
        for m in range(nc, nc+3):
            if maps[n][m] == num:
                return False
    return True


maps = [list(map(int, input())) for _ in range(9)]
blanks = []
for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            blanks.append((i, j))


def sudoku(cnt):
    if cnt == len(blanks):
        for m in maps:
            print(''.join(map(str, m)))
        exit(0)
    r, c = blanks[cnt]
    for i in range(1, 10):
        if garo(r, i) and sero(c, i) and nine(r, c, i):
            maps[r][c] = i
            sudoku(cnt+1)
            maps[r][c] = 0


sudoku(0)