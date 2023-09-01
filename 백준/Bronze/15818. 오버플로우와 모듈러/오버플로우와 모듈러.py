import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
dap = 1
for l in lst:
    dap *= (l%M)
    dap %= M
print(dap)