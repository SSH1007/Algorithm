N = int(input())
S = input()
dic = dict()
for s in S:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1
lst = list(dic.items())
lst.sort(key=lambda x: -x[1])
print(lst[0][0], lst[0][1])