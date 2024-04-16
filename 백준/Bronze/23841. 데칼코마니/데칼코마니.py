N, M = map(int, input().split())
pic = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if pic[i][j] != '.':
            pic[i][M-1-j] = pic[i][j]

for p in pic:
    print(*p, sep='')