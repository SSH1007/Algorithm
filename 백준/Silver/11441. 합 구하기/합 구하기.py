import sys
input = sys.stdin.readline
N = int(input().rstrip())
As = list(map(int, input().rstrip().split()))
hap = [0]*(N+1)
for n in range(N):
    hap[n+1] = As[n]+hap[n]
M = int(input().rstrip())
for _ in range(M):
    i, j = map(int, input().rstrip().split())
    print(hap[j]-hap[i-1])