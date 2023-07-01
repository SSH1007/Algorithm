import sys
input = sys.stdin.readline
As = list(map(int, input().rstrip().split()))
Bs = list(map(int, input().rstrip().split()))
As.sort(reverse=True)
Bs.sort(reverse=True)
dap = 0
for i in range(3):
    dap += (As[i]*Bs[i])
print(dap)