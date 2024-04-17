import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
c = 1
dap = 0
for l in lst:
    if c == l:
        c += 1
    else:
        dap += 1
print(dap)