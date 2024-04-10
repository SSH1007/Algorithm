X, Y, P1, P2 = map(int, input().split())
cnt = 0
while 1:
    if cnt > 1000:
        print(-1)
        break
    if P1 == P2:
        print(P1)
        break
    if P1 > P2:
        P2 += Y
    else:
        P1 += X
    cnt += 1