dic = dict()
for _ in range(10):
    n = int(input())
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
avgN, modeN = 0, 0
for d in dic.items():
    avgN+=d[0]*d[1]
avgN = avgN//10
lst = list(dic.items())
lst.sort(key=lambda i: i[1], reverse=True)
print(avgN, lst[0][0], sep='\n')