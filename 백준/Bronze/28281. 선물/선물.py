N, X = map(int, input().split())
lst = list(map(int, input().split()))
dap = []
for n in range(N-1):
    dap.append(lst[n]*X+lst[n+1]*X)
print(min(dap))