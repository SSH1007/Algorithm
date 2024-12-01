import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
Vs = list(map(int, input().split()))[::-1]
tmp, dap = 1, 0
for n in range(N):
    tmp = min(tmp, Vs[n])
    dap += tmp
    tmp += 1
print(dap)