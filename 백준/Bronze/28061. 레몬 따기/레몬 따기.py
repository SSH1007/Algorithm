import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = 0
for i in range(N):
    dap = max(dap, lst[i]-(N-i))
print(dap)