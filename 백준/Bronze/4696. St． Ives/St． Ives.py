while 1:
    n = float(input())
    if int(n) == 0:
        break
    print('%.2f' % (1+n+n**2+n**3+n**4))