M, N = map(int, input().split())
cnt = 0
matrix = list([0]*N for _ in range(M))

# 달팽이 이동 델타탐색
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
f = 0
# 시작 좌표
r, c = 0, 0

for i in range(1, M*N+1):
    matrix[r][c] = i
    r += dr[f]
    c += dc[f]
    if r < 0 or r >= M or c < 0 or c >= N or matrix[r][c]:
        r -= dr[f]
        c -= dc[f]
        f = (f+1) % 4
        r += dr[f]
        c += dc[f]
        cnt += 1

print(cnt-1)