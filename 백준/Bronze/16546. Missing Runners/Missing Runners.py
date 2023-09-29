import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = N*(N+1)//2 
for l in lst:
    dap -= l
print(dap)