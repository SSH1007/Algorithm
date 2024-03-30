N = int(input())
cookie = [list(input()) for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]


def findHeart():
    for i in range(1, N-1):
        for j in range(1, N-1):
            cnt = 0
            for k in range(4):
                if cookie[i+dr[k]][j+dc[k]] != '_':
                    cnt += 1
            if cnt == 4:
                return (i, j)


Hr, Hc = findHeart()
print(Hr+1, Hc+1)

waistR, waistC = 0, 0
for i in range(3):
    tmpR, tmpC = Hr, Hc
    cnt = 0
    while 1:
        if 0 <= tmpR+dr[i] < N and 0 <= tmpC+dc[i] < N:
            if cookie[tmpR+dr[i]][tmpC+dc[i]] == '*':
                tmpR += dr[i]
                tmpC += dc[i]
                cnt += 1
            else:
                break
        else:
            break
    if i == 2:
        waistR = tmpR
        waistC = tmpC
    print(cnt, end = ' ')

lr, lc, ll = waistR+1, waistC-1, 0
rr, rc, rl = waistR+1, waistC+1, 0
for i in range(lr, N):
    if cookie[i][lc] != '*':
        break
    else:
        ll += 1
print(ll, end = ' ')
for i in range(rr, N):
    if cookie[i][rc] != '*':
        break
    else:
        rl += 1
print(rl)