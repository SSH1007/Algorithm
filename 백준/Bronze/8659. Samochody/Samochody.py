import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
prefixSum = [0]*(n+1)
zeroIndexlst = []
for i in range(n):
    if lst[i] == 0:
        zeroIndexlst.append(i)
    prefixSum[i+1] = prefixSum[i] + lst[i]
dap = 0
for z in zeroIndexlst:
    dap += (prefixSum[n]-prefixSum[z])
print(dap)