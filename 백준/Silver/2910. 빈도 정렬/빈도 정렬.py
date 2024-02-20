import sys
input = sys.stdin.readline
N, C = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
dic = {}
for i in range(N):
    if not lst[i] in dic:
        dic[lst[i]] = 1
    else:
        dic[lst[i]] += 1
order = list(dic.keys())
nst = sorted(dic.items(), key=lambda x: (-x[1], order.index(x[0])))
for n in nst:
    for _ in range(n[1]):
        print(n[0], end = ' ')