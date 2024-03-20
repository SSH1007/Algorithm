N = int(input())
lst = sorted(list(map(int, input().split())), reverse=True)
dap = 0
for i in range(N-1):
    dap += lst[i+1] * lst[i]
    lst[i+1] = lst[i+1] + lst[i]
print(dap)