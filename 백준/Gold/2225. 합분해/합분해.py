N, K = map(int, input().split())
maps = [[0]*(N+1) for _ in range(K+1)]
# N:6, K:4까지 그려본 결과, 점화식은 maps[k][n] = maps[k-1][n] + maps[n][k-1]
for n in range(1, N+1):
    maps[1][n] = 1
for k in range(1, K+1):
    maps[k][1] = k
for k in range(2, K+1):
    for n in range(2, N+1):
        maps[k][n] = (maps[k-1][n] + maps[k][n-1]) % 1000000000
print(maps[K][N])