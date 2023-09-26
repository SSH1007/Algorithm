while 1:
    a = float(input())
    if a == 0:
        break
    dap, n, cnt = 0, 2, 1
    while dap < a:
        dap += 1/n
        n += 1
        cnt += 1
    print('%d card(s)' % (cnt-1))