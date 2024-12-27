import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
ice.sort(key=lambda x: x[1])
maps = [0]*(ice[-1][1]+1)
for ic in ice:
    maps[ic[1]] = ic[0]
for n in range(1, ice[-1][1]+1):
    maps[n] += maps[n-1]
maps = [0]+maps
dap = 0
for i in range(1, ice[-1][1]+2):
    s, e = i-K, i+K
    if s < 1:
        s = 1
    if e > ice[-1][1]+1:
        e = ice[-1][1]+1
    if dap < maps[e]-maps[s-1]:
        dap = maps[e]-maps[s-1]
print(dap)