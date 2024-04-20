import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = 0
hap = sum(lst)
for i in range(N):
    hap -= lst[i]
    dap += lst[i]*hap
print(dap)