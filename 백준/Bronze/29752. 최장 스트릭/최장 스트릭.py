N = int(input())
lst = list(map(int, input().split()))
dap = []
cnt = 0
for l in lst:
    if l:
        cnt += 1
    else:
        dap.append(cnt)
        cnt = 0
else:
    dap.append(cnt)
print(max(dap))