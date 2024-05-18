import sys
input = sys.stdin.readline
N, d, k, c = map(int, input().rstrip().split())
belt = []
for _ in range(N):
    belt.append(int(input().rstrip()))
belt = belt+belt

dap = 0
s, e = 0, k
for _ in range(N):
    bb = belt[s:e]
    s += 1
    e += 1
    if c not in bb:
        dap = max(dap, len(set(bb))+1)
    else:
        dap = max(dap, len(set(bb)))


print(dap)