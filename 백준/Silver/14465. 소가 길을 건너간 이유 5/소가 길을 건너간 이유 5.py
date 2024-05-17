import sys
input = sys.stdin.readline
N, K, B = map(int, input().rstrip().split())
road = [1 for _ in range(1, N+1)]
broken = set()
for _ in range(B):
    b = int(input().rstrip())
    broken.add(b)
    road[b-1] = 0

s, e = 0, K
d = sum(road[s:e])
dap = K-d
while e <= N:
    d -= road[s]
    s += 1
    if e >= N:
        break
    d += road[e]
    e += 1
    dap = min(dap, K-d)
print(dap)