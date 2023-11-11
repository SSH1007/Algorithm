s = [0,0,0,0,0]
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    if Y == 1 or Y == 2:
        s[0] += 1
    elif (Y == 3 or Y == 4) and S == 0:
        s[1] += 1
    elif (Y == 3 or Y == 4) and S == 1:
        s[2] += 1
    elif (Y == 5 or Y == 6) and S == 0:
        s[3] += 1
    elif (Y == 5 or Y == 6) and S == 1:
        s[4] += 1
dap = 0
import math
for st in s:
    dap += math.ceil(st/K)
print(dap)