N = int(input())
dap = [0]*N
lst = list(map(int, input().split()))
for n in range(N):
    cnt = 0
    for m in range(N):
        if cnt == lst[n] and dap[m] == 0:
            dap[m] = n+1
            break
        elif dap[m] == 0:
            cnt += 1

print(*dap)