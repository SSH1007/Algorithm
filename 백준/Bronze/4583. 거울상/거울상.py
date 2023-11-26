mirror = {'b':'d', 'd':'b', 'p':'q', 'q':'p', 'i':'i', 'o':'o', 'v':'v', 'w':'w', 'x':'x'}
while 1:
    S = input()
    if S == '#':
        break
    dap = ''
    for s in S:
        if s not in mirror:
            print('INVALID')
            break
        if s in mirror:
            dap += mirror[s]
    else:
        print(dap[::-1])