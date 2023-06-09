import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
dap = ((a*b)/4840)/5
if dap%1 == int(dap):
    print(dap)
else:
    print(int(dap)+1)