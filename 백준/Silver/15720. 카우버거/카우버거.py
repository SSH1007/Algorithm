B, S, D = map(int, input().split())
l = max(B, S, D)
burger = list(map(int, input().split()))
for _ in range(l-B):
    burger.append(0)
burger.sort()
side = list(map(int, input().split()))
for _ in range(l-S):
    side.append(0)
side.sort()
drink = list(map(int, input().split()))
for _ in range(l-D):
    drink.append(0)
drink.sort()
hap1, hap2 = 0, 0
for i in range(l):
    hap1 += (burger[i]+side[i]+drink[i])
    if 0 == burger[i] or 0 == side[i] or 0 == drink[i]:
        hap2 += (burger[i]+side[i]+drink[i])
    else:
        hap2 += (burger[i] + side[i] + drink[i])*0.9
print(hap1, int(hap2), sep='\n')