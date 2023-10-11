while 1:
    lst = list(map(int, input().split()))
    if sum(lst) == 0:
        break
    lst.sort()
    dap = sum(lst[1:5])/4
    if dap%1:
        print(dap)
    else:
        print(int(dap))