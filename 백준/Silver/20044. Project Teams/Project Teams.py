n = int(input())
lst = list(map(int, input().split()))
lst.sort()
dap = []
for i in range(n):
    dap.append(lst[i] + lst[2*n-1-i])
print(min(dap))