# 지구 E, 태양 S, 달 M
# 1<=E<=15, 1<=S<=28, 1<=M<=19
E, S, M = map(int, input().split())
year = 1
while 1:
    if (year-E)%15==0 and (year-S)%28==0 and (year-M)%19==0:
        break
    year+=1
print(year)
