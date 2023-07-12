N = int(input())
dap = 0
cows = dict()
for _ in range(N):
    num, point = map(int, input().split())
    if num not in cows:
        cows[num] = point
    else:
        if cows[num] != point:
            cows[num] = point
            dap+=1
print(dap)