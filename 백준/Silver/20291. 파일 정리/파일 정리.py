import sys
input = sys.stdin.readline
N = int(input().rstrip())
dic = {}
for _ in range(N):
    name = input().rstrip().split('.')
    if not name[1] in dic:
        dic[name[1]] = 1
    else:
        dic[name[1]] += 1
dap = sorted(list(dic.items()), key=lambda x:x[0])
for d in dap:
    print(d[0], d[1])