import sys
input = sys.stdin.readline
dap = 0
n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
lst.sort()
for i in range(1, n+1):
    dap += lst[i-1] * 2 * ((i-1) - (n-i))
print(dap)