C, R = map(int, input().split())
K = int(input())

seat = [[0]*C for _ in range(R)]

x = R-1
y = 0
seat[x][y] = 1

#     상  우 하  좌
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

cnt = 1
i = 0
while 1:
    seat[x][y] = cnt
    if cnt == K:
        print(y+1, R-x)
        break
    if cnt > C*R:
        print(0)
        break

    x += di[i]
    y += dj[i]
    if 0 > x or x >= R or 0 > y or y >= C or seat[x][y]:
        x -= di[i]
        y -= dj[i]
        i = (i+1) % 4
        x += di[i]
        y += dj[i]
    cnt += 1