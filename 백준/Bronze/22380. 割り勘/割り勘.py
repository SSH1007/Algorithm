while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    average = b//a
    money = list(map(int, input().split()))
    dap = 0
    for m in money:
        dap += min(average, m)
    print(dap)