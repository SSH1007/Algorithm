def solution(n):
    answer = [[0]*n for _ in range(n)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir = 0
    r, c = 0, 0
    for x in range(1, n*n+1):
        answer[r][c] = x
        fr = r+move[dir][0]
        fc = c+move[dir][1]
        if fr < 0 or fc < 0 or fr >= n or fc >= n or answer[fr][fc] != 0:
            dir = (dir+1)%4
            r += move[dir][0]
            c += move[dir][1]
        else:
            r = fr
            c = fc
    return answer