import sys
input = sys.stdin.readline
S = input().rstrip()
dic = []
for i in range(len(S)):
    dic.append(S[i:])
dic.sort()
for d in dic:
    print(d)