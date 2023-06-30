import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = 1
start = lst[0]
for n in range(1, N):
    if lst[n] >= start:
        dap+=1
        start = lst[n]
    else:
        start = lst[n]
print(dap)