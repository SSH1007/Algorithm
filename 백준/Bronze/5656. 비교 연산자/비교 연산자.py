dap = True
cnt = 1
while 1:
    a,b,c = input().split()
    a, c = int(a), int(c)
    if b == '>':
        dap = a > c
    elif b == '>=':
        dap = a >= c
    elif b == '<':
        dap = a < c
    elif b == '<=':
        dap = a <= c
    elif b == '==':
        dap = a == c
    elif b == '!=':
        dap = a != c
    elif b == 'E':
        break
    print(f'Case {cnt}: {str(dap).lower()}')
    cnt += 1