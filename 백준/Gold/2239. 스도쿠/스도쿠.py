import sys
input = lambda: sys.stdin.readline().rstrip()

row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
square_used = [set() for _ in range(9)]


def get_square_idx(r, c):
    return (r//3)*3 + (c//3)


maps = [list(map(int, input())) for _ in range(9)]
blanks = []
for i in range(9):
    for j in range(9):
        if maps[i][j] == 0:
            blanks.append((i, j))
        else:
            num = maps[i][j]
            row_used[i].add(num)
            col_used[j].add(num)
            square_used[get_square_idx(i, j)].add(num)


def sudoku(cnt):
    if cnt == len(blanks):
        for m in maps:
            print(''.join(map(str, m)))
        exit(0)

    r, c = blanks[cnt]
    square_num = get_square_idx(r, c)
    for i in range(1, 10):
        if i not in row_used[r] and \
            i not in col_used[c] and \
            i not in square_used[square_num]:
            maps[r][c] = i
            row_used[r].add(i)
            col_used[c].add(i)
            square_used[square_num].add(i)

            sudoku(cnt+1)

            maps[r][c] = 0
            row_used[r].discard(i)
            col_used[c].discard(i)
            square_used[square_num].discard(i)


sudoku(0)