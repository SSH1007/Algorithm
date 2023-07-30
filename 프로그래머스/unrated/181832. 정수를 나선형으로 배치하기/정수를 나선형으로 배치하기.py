def solution(n):
    answer = [[0]*n for _ in range(n)]
    r, c = 0, 0
    num = 1
    direction = 1
    while num <= n*n:
        if answer[r][c] == 0:
            answer[r][c] = num
        if num == n*n:
            break
        if direction == 1:
            if c < n-1 and not answer[r][c+1]:
                c += 1
            else:
                direction = 2
                continue
        elif direction == 2:
            if r < n-1 and not answer[r+1][c]:
                r += 1
            else:
                direction = 3
                continue
        elif direction == 3:
            if c > 0 and not answer[r][c-1]:
                c -= 1
            else:
                direction = 4
                continue
        elif direction == 4:
            if r > 0 and not answer[r-1][c]:
                r -= 1
            else:
                direction = 1
                continue
        num += 1

    return answer