import sys
input = sys.stdin.readline
N = int(input().rstrip())
board = [list(input().rstrip()) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
answer = 0


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


def f(k, r, c, nr, nc):
    dap = 0
    if k%2: # 상하교환
        tmp = []
        for n in range(N):
            tmp.append(board[n][c])
        dap = max(dap, long(tmp))
        dap = max(dap, long(board[r]))
        dap = max(dap, long(board[nr]))
    else:   # 좌우교환
        tmp = []
        for n in range(N):
            tmp.append(board[n][c])
        dap = max(dap, long(tmp))
        tmp = []
        for n in range(N):
            tmp.append(board[n][nc])
        dap = max(dap, long(tmp))
        dap = max(dap, long(board[r]))
    return dap


for i in range(N):
    for j in range(N):
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < N and 0 <= nc < N:
                board[i][j], board[nr][nc] = board[nr][nc], board[i][j]
                answer = max(answer, f(k, i, j, nr, nc))
                board[i][j], board[nr][nc] = board[nr][nc], board[i][j]
print(answer)