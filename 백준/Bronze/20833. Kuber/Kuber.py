import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for n in range(1, N+1):
    dap += (n**3)
print(dap)