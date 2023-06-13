import sys
input = sys.stdin.readline
n = int(input().rstrip())
K = 0
sw = list(map(int, input().rstrip().split()))
swPrefixSum = [0]*(n+1)
for i in range(n):
    swPrefixSum[i+1] = swPrefixSum[i] + sw[i]
se = list(map(int, input().rstrip().split()))
sePrefixSum = [0]*(n+1)
for i in range(n):
    sePrefixSum[i+1] = sePrefixSum[i] + se[i]

for i in range(1,n+1):
    if swPrefixSum[i] == sePrefixSum[i]:
        if K<i:
            K=i

print(K)