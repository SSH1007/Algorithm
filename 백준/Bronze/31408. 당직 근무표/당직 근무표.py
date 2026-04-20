N =  int(input())
lst = list(map(int, input().split()))
dic = dict()
for l in lst:
    if not l in dic:
        dic[l] = 1
    else:
        dic[l] += 1
mx = sorted(list(dic.values()))[-1]
print('NO' if N-mx < mx-1 else 'YES')