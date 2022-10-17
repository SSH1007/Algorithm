import sys
input = sys.stdin.readline

N, M = map(int,input().split())
numbers = list(map(int, input().split()))
sums = [0 for _ in range(N+1)]
sums[1] = numbers[0]
for n in range(2,N+1):
    sums[n] = sums[n-1]+numbers[n-1]

for _ in range(M):
    s,e = map(int, input().split())
    print(sums[e]-sums[s-1])