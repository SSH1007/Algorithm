import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(float, input().rstrip().split()))
dap = 0
for l in lst:
    dap += (l**3)
print(dap**(1.0/3.0))