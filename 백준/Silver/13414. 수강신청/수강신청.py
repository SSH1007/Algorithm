import sys
input = sys.stdin.readline
K, L = map(int, input().rstrip().split())
dic = dict()
for _ in range(L):
    a = input().rstrip()
    if a in dic:
        dic.pop(a)
    dic[a] = 1
lst = list(dic.keys())
for l in lst[:K]:
    print(l)