import sys
input = sys.stdin.readline
N, K, B = map(int, input().rstrip().split())
road = [0 for _ in range(1, N+1)]
for _ in range(B):
    road[int(input().rstrip())-1] = 1

s, e = 0, K
dap = sum(road[s:e])
tmp = dap
for i in range(1, N-K+1):
    if road[i-1]:
        tmp -= 1
    if road[i+K-1]:
        tmp += 1
    dap = min(dap, tmp)
print(dap)