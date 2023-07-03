import sys
input = sys.stdin.readline
n = int(input().rstrip())
dap = []
for i in range(1, n+1):
    if n%i==0:
        dap.append(i)
print(sum(dap)*5-24)