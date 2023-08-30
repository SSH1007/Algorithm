N = int(input())
dap = 0
lst = []
for _ in range(N):
    lst.append(int(input()))
for i in range(N-1, 0, -1):
    if lst[i] <= lst[i-1]:
        tmp = lst[i-1]-lst[i]+1
        dap += tmp
        lst[i-1] = lst[i-1]-tmp
print(dap)