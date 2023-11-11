s12 = 0
sm34 = 0
sm56 = 0
sf34 = 0
sf56 = 0
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    if Y == 1 or Y == 2:
        s12 += 1
    elif (Y == 3 or Y == 4) and S == 0:
        sf34 += 1
    elif (Y == 3 or Y == 4) and S == 1:
        sm34 += 1
    elif (Y == 5 or Y == 6) and S == 0:
        sf56 += 1
    elif (Y == 5 or Y == 6) and S == 1:
        sm56 += 1
dap = 0
dap += (s12//K + s12%K)
dap += (sm34//K + sm34%K)
dap += (sm56//K + sm56%K)
dap += (sf34//K + sf34%K)
dap += (sf56//K + sf56%K)
print(dap)