N = int(input())
lst = list(map(int, input().split()))

_set = set(lst)
_lst = sorted(list(_set))

# 딕셔너리로 만들어서 바로 조회하도록 함
dic = dict()
for l in range(len(_lst)):
    if _lst[l] not in dic:
        dic[_lst[l]] = l

for l in lst:
    print(dic[l], end=' ')