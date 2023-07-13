N = int(input())
dic = dict()
for _ in range(N):
    S = input()
    if S not in dic:
        dic[S] = 1
    else:
        dic[S] += 1
lst = list(dic.items())
lst.sort(key = lambda x:(-x[1],x[0]))
print(lst[0][0])