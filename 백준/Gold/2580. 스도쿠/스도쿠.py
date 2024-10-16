import sys
input = lambda: sys.stdin.readline().rstrip()

maps = [list(map(int, input().split())) for _ in range(9)]

row_used = [0]*9
col_used = [0]*9
nine_used = [0]*9


def getNineNum(r, c):
    return (r//3)*3+c//3


blanks = []
for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            blanks.append((i, j))
        else:
            num = maps[i][j]
            idx = getNineNum(i, j)
            row_used[i] |= (1 << num)
            col_used[j] |= (1 << num)
            nine_used[idx] |= (1 << num)


def sudoku(cnt):
    if cnt == len(blanks):
        for m in maps:
            print(*m)
        exit(0)
    r, c = blanks[cnt]
    n = getNineNum(r, c)
    bitmask = row_used[r] | col_used[c] | nine_used[n]
    for num in range(1, 10):
        if not bitmask & (1 << num):

            row_used[r] |= (1 << num)
            col_used[c] |= (1 << num)
            nine_used[n] |= (1 << num)
            maps[r][c] = num

            sudoku(cnt + 1)

            row_used[r] &= ~(1 << num)
            col_used[c] &= ~(1 << num)
            nine_used[n] &= ~(1 << num)
            maps[r][c] = 0


sudoku(0)