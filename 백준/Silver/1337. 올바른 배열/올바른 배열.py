N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
dap = []
for l in lst:
    tmp = 0
    for i in range(l, l+5):
        if i not in lst:
            tmp += 1
    dap.append(tmp)
print(min(dap))