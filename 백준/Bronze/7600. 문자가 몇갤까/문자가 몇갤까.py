while 1:
    S = input().upper()
    if S == '#':
        break
    lst = []
    for s in S:
        if s not in lst and s in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            lst.append(s)
    print(len(lst))