lst = []
for _ in range(3):
    lst.append(input()+'.')
for i in range(3):
    dap = []
    tmp = ''
    for l in range(len(lst[i])-1):
        if lst[i][l] == lst[i][l+1]:
            tmp += lst[i][l]
        else:
            dap.append(tmp)
            tmp = ''

    result = 0
    for d in dap:
        result = max(result, len(d))
    print(result+1)