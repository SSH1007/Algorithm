N, R, C = map(int, input().split())
farm = [[0]*N for _ in range(N)]
for i in range((R-1)%2, N, 2):
    for j in range((C-1)%2, N, 2):
        farm[i][j] = 1
for i in range(R%2, N, 2):
    for j in range(C%2, N, 2):
        farm[i][j] = 1
for fl in farm:
    for f in fl:
        if f:
            print('v', end='')
        else:
            print('.', end='')
    print()