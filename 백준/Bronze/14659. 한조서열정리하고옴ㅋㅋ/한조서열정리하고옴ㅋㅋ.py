N = int(input())
archers = list(map(int, input().split()))
dap = 0
highest = 0
for n in range(N-1):
    highest = max(highest, archers[n])
    kill = 0
    if archers[n] == highest:
        for m in range(n+1, N):
            if archers[n] > archers[m]:
                kill += 1
            elif archers[n] < archers[m]:
                break
        dap = max(dap, kill)
print(dap)