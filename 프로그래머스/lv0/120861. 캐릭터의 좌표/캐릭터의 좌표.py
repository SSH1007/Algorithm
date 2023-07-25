def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    M, N = board[0], board[1]
    for k in keyinput:
        if k == 'left' and x-1 >= (M//2)*-1:
            x -= 1
        elif k == 'right' and x+1 <= M//2:
            x += 1
        elif k == 'up' and y+1 <= N//2:
            y += 1
        elif k == 'down' and y-1 >= (N//2)*-1:
            y -= 1
    answer = [x,y]
    return answer