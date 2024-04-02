S, K = map(int, input().split())
sk = S//K
rest = S%K
lst = [sk]*K
for r in range(rest):
    lst[r] += 1
dap = 1
for l in lst:
    dap *= l
print(dap)