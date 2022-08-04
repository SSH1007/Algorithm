while 1:
    N=input()
    dc=dict()
    if N=='*':
        break
    for n in N:
        if n == ' ':
            continue
        if n in dc:
            dc[n]+=1
        else:
            dc[n]=1
    if len(dc)==26:
        print('Y')
    else:
        print('N')