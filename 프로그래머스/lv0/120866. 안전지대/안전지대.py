def solution(board):
    answer = 0
    N = len(board)
    for n in range(N):
        for m in range(N):
            if board[n][m] == 1:
                if n-1 >= 0:
                    if board[n-1][m] == 0:
                        board[n-1][m] = 2
                if n-1 >= 0 and m-1 >= 0:
                    if board[n-1][m-1] == 0:
                        board[n-1][m-1] = 2
                if n-1 >= 0 and m+1 < N:
                    if board[n-1][m+1] == 0:
                        board[n-1][m+1] = 2
                if m+1 < N:
                    if board[n][m+1] == 0:
                        board[n][m+1] = 2
                if m-1 >= 0:
                    if board[n][m-1] == 0:
                        board[n][m-1] = 2
                if n+1 < N:
                    if board[n+1][m] == 0:
                        board[n+1][m] = 2
                if n+1 < N and m-1 >= 0:
                    if board[n+1][m-1] == 0:
                        board[n+1][m-1] = 2
                if n+1 < N and m+1 <N:
                    if board[n+1][m+1] == 0:
                        board[n+1][m+1] = 2

    for b in board:
        answer += b.count(0)
    return answer