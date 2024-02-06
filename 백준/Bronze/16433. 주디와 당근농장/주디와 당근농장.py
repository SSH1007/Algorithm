N, R, C = map(int, input().split())
farm = [['.']*N for _ in range(N)]
carrot = (R+C)%2
for i in range(N):
    for j in range(N):
        if (i+j)%2 == carrot:
            farm[i][j] = 'v'
for f in farm:
    print(*f, sep='')