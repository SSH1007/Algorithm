X, L, R = map(int, input().split())
lst = list(range(L,R+1))
cha = 1e9
dap = 0
for l in lst:
    if abs(l-X) <= cha:
        cha = abs(l-X)
        dap = l
print(dap)