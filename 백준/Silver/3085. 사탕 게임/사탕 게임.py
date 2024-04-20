import sys
input = sys.stdin.readline
N = int(input().rstrip())
board = [list(input().rstrip())+['.'] for _ in range(N)] + [['.']*(N+1)]
board_t = list(map(list, zip(*board)))


def long(lst_):
    dap = 0
    tmp = 0
    for c in ['C', 'P', 'Z', 'Y']:
        lst = [0]
        for l in lst_:
            if l == c:
                tmp += 1
            else:
                lst.append(tmp)
                tmp = 0
        lst.append(tmp)
        dap = max(max(lst), dap)
        tmp = 0
    return dap


def f(lst):
    dap = 0
    for i in range(N-1):
        for j in range(N):
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            dap = max(dap, long(lst[i]))
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]

            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
            dap = max(dap, long(lst[i]), long(lst[i+1]))
            lst[i][j], lst[i+1][j] = lst[i+1][j], lst[i][j]
    return dap


answer = max(f(board), f(board_t))
print(answer)