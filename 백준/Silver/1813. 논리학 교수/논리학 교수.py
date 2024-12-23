N = int(input())
lst = list(map(int, input().split()))
dap = -1
for i in range(N):
    if lst.count(lst[i]) == lst[i]:
        dap = max(dap, lst[i])
if dap == -1 and lst.count(0) == 0:
    dap = 0
print(dap)