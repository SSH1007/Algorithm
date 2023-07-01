import sys
input = sys.stdin.readline
N = int(input().rstrip())
N = 100-N
dap = []
for i in [25, 10, 5, 1]:
    dap.append(N//i)
    N%=i
print(*dap)