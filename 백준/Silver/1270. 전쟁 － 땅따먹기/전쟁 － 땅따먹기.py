import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    Ti = lst[0]
    soldiers = lst[1:]
    dic = {}
    for t in range(Ti):
        if not soldiers[t] in dic:
            dic[soldiers[t]] = 1
        else:
            dic[soldiers[t]] += 1
    sd = sorted(dic.items(), key= lambda x:-x[1])
    if sd[0][1] > Ti//2:
        print(sd[0][0])
    else:
        print('SYJKGW')