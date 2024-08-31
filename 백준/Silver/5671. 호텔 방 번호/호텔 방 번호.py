while 1:
    try:
        N, M = map(int, input().split())
        dap = 0
        for num in range(N, M+1):
            i = list(str(num))
            if len(i) == len(set(i)):
                dap += 1
        print(dap)
    except:
        break