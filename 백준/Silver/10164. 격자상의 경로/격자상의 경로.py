N, M, K = map(int, input().split())
if K == 0:
    Kr, Kc = N, M
else:
    Kr = K//M + (1 if K % M else 0)
    Kc = K-(Kr-1)*M

grid = [[0]*(M+1) for _ in range(N+1)]
grid[0][1] = 1
for n in range(1, Kr+1):
    for m in range(1, Kc+1):
        grid[n][m] = grid[n-1][m] + grid[n][m-1]
tmp = 1
if K != 0:
    tmp = grid[Kr][Kc]
    grid[Kr][Kc] = 0
    for n in range(Kr, N+1):
        for m in range(Kc, M+1):
            grid[n][m] = grid[n-1][m] + grid[n][m-1]
print(grid[N][M])