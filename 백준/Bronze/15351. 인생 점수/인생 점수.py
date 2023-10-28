T = int(input())
for _ in range(T):
    Q = input()
    dap = 0
    for q in Q:
        if q != ' ':
            dap += (ord(q)-64)
    if dap == 100:
        print('PERFECT LIFE')
    else:
        print(dap)