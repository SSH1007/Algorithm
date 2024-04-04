import sys
input = sys.stdin.readline
N = int(input().rstrip())
dic = dict()
for _ in range(N):
    name = input().rstrip()
    if not name in dic:
        dic[name] = 1
    else:
        dic[name] += 1
for _ in range(N-1):
    name = input().rstrip()
    dic[name] -= 1
print(sorted(list(dic.items()), key=lambda x: x[1], reverse=True)[0][0])