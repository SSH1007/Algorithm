import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = lst[0]
for i in range(1, N):
    if lst[i]-lst[i-1] != 1:
        dap += lst[i]
print(dap)