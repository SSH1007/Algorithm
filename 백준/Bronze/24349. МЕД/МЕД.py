import sys
input = sys.stdin.readline
n, a, b, c = map(int, input().rstrip().split())
dap = 0
if n>1:
    if a<c or b<c :
        dap = (n-1)*min(a,b)
    else:
        dap = min(a,b)+(n-2)*c
print(dap//100, dap%100)