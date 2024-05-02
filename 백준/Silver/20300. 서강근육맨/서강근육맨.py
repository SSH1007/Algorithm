import sys
input = sys.stdin.readline
N = int(input().rstrip())
ts = sorted(list(map(int, input().rstrip().split())))
dap = 0
if N % 2:
    dap = ts.pop()
lst = [ts[i]+ts[len(ts)-i-1] for i in range(N//2)]
lst.append(dap)
print(max(lst))