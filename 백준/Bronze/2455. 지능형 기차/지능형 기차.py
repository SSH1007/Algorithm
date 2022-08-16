saram = 0
maxsaram = 0
for _ in range(4):
    naerim, tam = map(int,input().split())
    saram-=naerim
    saram+=tam
    if maxsaram < saram:
        maxsaram = saram
print(maxsaram)