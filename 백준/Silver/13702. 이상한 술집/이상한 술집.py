import sys
input = lambda: sys.stdin.readline().rstrip()


N, K = map(int, input().split())
kettles = []
for _ in range(N):
    kettles.append(int(input()))
s, e = 0, 2**31-1
dap = 0
while s <= e:
    mid = (s+e)//2
    tmp = 0
    for k in kettles:
        tmp += k//mid
    if tmp >= K:
        s = mid + 1
        dap = mid
    else:
        e = mid - 1
print(dap)