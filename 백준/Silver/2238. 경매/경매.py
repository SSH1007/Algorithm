import sys
input = sys.stdin.readline
U, N = map(int, input().rstrip().split())
dic = {}
lst = []
for n in range(N):
    S, P = input().rstrip().split()
    P = int(P)
    if P not in dic:
        dic[P] = 1
    else:
        dic[P] += 1
    lst.append((S, P, n))
dicItem = list(dic.items())
minDeal = min(list(dic.values()))
first = [i for i in dicItem if i[1] == minDeal]
first.sort(key=lambda x: x[0])

minPrice = first[0]
second = [i for i in lst if i[1] == minPrice[0]]
second.sort(key=lambda x:x[2])
print(second[0][0], second[0][1])