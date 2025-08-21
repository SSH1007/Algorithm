N = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
dap = 0
for n in range(N):
    if As[n] > Bs[n]:
        dap += 3
    elif As[n] == Bs[n]:
        dap += 1
print(dap)