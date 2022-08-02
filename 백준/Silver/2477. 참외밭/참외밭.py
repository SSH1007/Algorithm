melon = int(input())
alst=''
blst=[]
clst=dict()
for _ in range(6):
    a,b=map(int,input().split())
    alst+=str(a)
    blst.append(b)
    if a in clst:
        clst[a]+=b
    else:
        clst[a]=b
findcase = [24,13,32,41]
for fc in findcase:
    if alst.find(str(fc))>=0:
        break
fp = alst.find(str(fc))
print(melon*(max(clst.values())*min(clst.values())-blst[fp]*blst[fp+1]))
