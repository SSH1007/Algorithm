import sys
input = sys.stdin.readline
N = int(input().rstrip())
dic = dict()
for _ in range(N):
    a = int(input().rstrip())
    if a not in dic:
        dic[a] = 1
    else:
        dic[a] += 1
lst = list(dic.items())
lst.sort(key=lambda x: (-x[1], x[0]))
print(lst[0][0])