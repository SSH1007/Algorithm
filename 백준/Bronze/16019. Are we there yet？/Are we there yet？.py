import sys
input = sys.stdin.readline
lst = list(map(int, input().rstrip().split()))
prefixSum = [0]*5
for n in range(len(lst)):
    prefixSum[n+1] = prefixSum[n] + lst[n]

dap = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        dap[i][j] = abs(prefixSum[i]-prefixSum[j])
for d in dap:
    print(*d)