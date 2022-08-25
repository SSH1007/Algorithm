N = int(input())
Pillar = []
for _ in range(N):
    L, H = map(int,input().split())
    Pillar.append((L,H))

# 제일 높은 높이 찾기
hPillar = sorted(Pillar, key = lambda x:x[1])
lPillar = sorted(Pillar, key = lambda x:x[0])
std = lPillar.index(hPillar[-1])

# 가장 높은 놈 미만까지 더하기
dap = 0
curhighest = 0
for i in range(std):
    curhighest = max(curhighest,lPillar[i][1])
    for j in range(lPillar[i][0],lPillar[i+1][0]):
        dap += curhighest

# 가장 높은 놈 더하기
dap+=lPillar[std][1]

# 가장 높은 놈 초과부터 더하기
curhighest = 0
for i in range(len(lPillar)-1,std,-1):
    curhighest = max(curhighest,lPillar[i][1])
    for j in range(lPillar[i-1][0],lPillar[i][0]):
        dap+=curhighest
print(dap)