import sys
input = lambda: sys.stdin.readline().rstrip()

row_used = [0]*9
col_used = [0]*9
square_used = [0]*9


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
            row_used[i] |= (1 << num)
            col_used[j] |= (1 << num)
            square_used[get_square_idx(i, j)] |= (1 << num)


def sudoku(cnt):
    if cnt == len(blanks):
        for m in maps:
            print(''.join(map(str, m)))
        exit(0)

    r, c = blanks[cnt]
    square_num = get_square_idx(r, c)
    # bitmask는 현재 사용된 수들을 의미
    bitmask = row_used[r] | col_used[c] | square_used[square_num]

    for i in range(1, 10):
        # bitmask에 아직 i가 사용되지 않았다면
        if not (bitmask & (1 << i)):
            maps[r][c] = i
            row_used[r] |= (1 << i)
            col_used[c] |= (1 << i)
            square_used[square_num] |= (1 << i)

            sudoku(cnt+1)

            maps[r][c] = 0
            row_used[r] &= ~(1 << i)
            col_used[c] &= ~(1 << i)
            square_used[square_num] &= ~(1 << i)


sudoku(0)