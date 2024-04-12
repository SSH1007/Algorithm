import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    D, C = map(int, input().rstrip().split())
    lst.append((D, C))
lst.sort()
dap = 0
cost = 10001
for l in lst:
    c = l[1]
    if cost > c:
        cost = c
        dap += 1
print(dap)