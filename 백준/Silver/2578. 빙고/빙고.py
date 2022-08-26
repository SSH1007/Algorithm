rbingo = [0]*5
cbingo = [0]*5
dbingo = [0]*2

bingo = []
for _ in range(5):
    bingo += list(map(int, input().split()))
    
mc = []
for _ in range(5):
    mc += list(map(int, input().split()))

cnt = 0
for m in mc:
    point = bingo.index(m)
    rbingo[point//5] += 1
    if (rbingo + cbingo + dbingo).count(5) >= 3:
        break
    cbingo[point % 5] += 1
    if (rbingo + cbingo + dbingo).count(5) >= 3:
        break
    if point//5 == point % 5:
        dbingo[0] += 1
        if (rbingo+cbingo+dbingo).count(5) >= 3:
            break
    if point//5 + point % 5 == 4:
        dbingo[1] += 1
        if (rbingo+cbingo+dbingo).count(5) >= 3:
            break
print(mc.index(m)+1)