import sys
input = sys.stdin.readline
N, M, R = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M)//2):
        r, c = i, i
        formerValue = matrix[r][c]
        nr, nc = i, i

        # down
        for j in range(r+1, N-r):
            nr = j
            value = matrix[nr][nc]
            matrix[nr][nc] = formerValue
            formerValue = value

        # right
        for j in range(c+1, M-c):
            nc = j
            value = matrix[nr][nc]
            matrix[nr][nc] = formerValue
            formerValue = value

        # up
        for j in range(N-r-2, r-1, -1):
            nr = j
            value = matrix[nr][nc]
            matrix[nr][nc] = formerValue
            formerValue = value

        # left
        for j in range(M-c-2, c-1, -1):
            nc = j
            value = matrix[nr][nc]
            matrix[nr][nc] = formerValue
            formerValue = value

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=' ')
    print()