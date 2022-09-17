h, v = map(int, input().split())
N = int(input())
garo, sero = [0], [0]
for _ in range(N):
    d, n  = map(int, input().split())
    if d:
        garo.append(n)
    else:
        sero.append(n)
garo.append(h)
sero.append(v)
garo.sort()
sero.sort()
maxh, maxv = 0, 0
for g in range(len(garo)-1):
    if maxh < garo[g+1]-garo[g]:
        maxh = garo[g+1]-garo[g]
for s in range(len(sero)-1):
    if maxv < sero[s+1]-sero[s]:
        maxv = sero[s+1]-sero[s]
print(maxh*maxv)