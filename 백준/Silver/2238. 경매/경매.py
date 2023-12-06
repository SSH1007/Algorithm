import sys
input = sys.stdin.readline
U, N = map(int, input().rstrip().split())
dic = {}
for n in range(N):
    S, P = input().rstrip().split()
    P = int(P)
    if P not in dic:
        dic[P] = [S]
    else:
        dic[P] += [S]

minChoice = min([len(i) for i in dic.values()])
minPrice = min([i for i in dic.keys() if len(dic[i]) == minChoice])
print(dic[minPrice][0], minPrice)