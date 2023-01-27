DD = list(map(int, input().split(':')))
dap = 0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if i == j or i == k or j == k:
                continue
            if 0<DD[i]<=12 and 0<=DD[j]<60 and 0<=DD[k]<60:
                dap+=1
print(dap) 