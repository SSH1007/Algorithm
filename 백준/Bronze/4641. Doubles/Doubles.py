while 1:
    lst = list(map(int, input().split()))
    if lst[0] == -1:
        break
    dap = 0
    lsst = [l*2 for l in lst[:-1]]
    for l in lsst:
        if l in lst:
            dap += 1
    print(dap)