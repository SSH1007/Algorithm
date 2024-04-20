import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = 0
for i in range(N):
    dap += lst[i]*sum(lst[i+1:])
print(dap)