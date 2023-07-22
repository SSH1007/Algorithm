import sys
input = sys.stdin.readline
N, C = map(int, input().rstrip().split())
dic = dict()
for _ in range(N):
    a = int(input().rstrip())
    if a == 1:
        print(C)
        quit(0)
    for i in range(a, C+1, a):
        if i not in dic:
            dic[i] = 1
print(len(dic))