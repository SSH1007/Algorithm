import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
dap = N
while N>0:
    N //= M
    dap += N
print(dap)