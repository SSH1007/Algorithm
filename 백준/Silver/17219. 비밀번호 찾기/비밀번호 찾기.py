import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
siteInfo = dict()
dap = []
for _ in range(N):
    a, b = input().rstrip().split()
    siteInfo[a] = b
for _ in range(M):
    c = input().rstrip()
    dap.append(siteInfo[c])
for d in dap:
    print(d)