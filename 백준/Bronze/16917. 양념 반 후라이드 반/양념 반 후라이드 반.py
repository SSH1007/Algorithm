import sys
input = sys.stdin.readline
A, B, C, X, Y = map(int, input().rstrip().split())
dap = 0
tmp = min(X,Y)
if A+B > C*2:
    dap += C*2*tmp
    X -= tmp
    Y -= tmp
if A > C*2:
    dap += C*2*X
else:
    dap += A*X
if B > C*2:
    dap += C*2*Y
else:
    dap += B*Y
print(dap)