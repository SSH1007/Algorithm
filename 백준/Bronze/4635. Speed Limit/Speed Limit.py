while 1:
    n = int(input())
    if n == -1:
        break
    lst = []
    for _ in range(n):
        s, t = map(int, input().split())
        lst.append((s, t))
    dap = lst[0][0]*lst[0][1]
    for i in range(1, n):
        dap += lst[i][0]*(lst[i][1]-lst[i-1][1])
    print(f'{dap} miles')