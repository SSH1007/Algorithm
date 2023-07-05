import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for _ in range(N):
    X = input().rstrip()
    dap += int(X[:-1])**int(X[-1])
print(dap)