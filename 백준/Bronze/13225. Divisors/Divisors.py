import sys
input = sys.stdin.readline
C = int(input().rstrip())
dap = []

def soinsu(n):
    dic = dict()
    d = 2
    while d <= n:
        if n % d == 0:
            if d not in dic:
                dic[d] = 1
            else:
                dic[d] += 1
        d += 1
    lst = dic.values()
    dap.append((n, len(lst)+1))

for _ in range(C):
    n = int(input().rstrip())
    soinsu(n)

for d in dap:
    print(*d)