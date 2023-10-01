W, N, P = map(int, input().split())
Ps = list(map(int, input().split()))
dap = 0
for p in Ps:
    if W<=p<=N:
        dap += 1
print(dap)