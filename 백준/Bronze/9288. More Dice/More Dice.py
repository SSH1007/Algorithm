N = int(input())
for n in range(1, N+1):
    x = int(input())
    print('Case %d:'%(n))
    for a in range(1, 7):
        for b in range(a, 7):
            if a+b == x:
                print('(%d,%d)'%(a, b))