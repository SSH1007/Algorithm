while 1:
    startTime, passTime = input().split()
    if startTime == '00:00' and passTime == '00:00':
        break
    sh, sm = map(int, startTime.split(':'))
    ph, pm = map(int, passTime.split(':'))
    eh = sh+ph
    em = sm+pm
    d = 0
    if em >= 60:
        eh += 1
        em -= 60
    if eh >= 24:
        d += eh//24
        eh %= 24
    if d:
        print('%02d:%02d +%d' % (eh, em, d))
    else:
        print('%02d:%02d' % (eh, em))