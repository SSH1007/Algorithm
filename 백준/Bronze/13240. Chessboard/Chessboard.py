R, C = map(int, input().split())
flag = True
for r in range(R):
    flag2 = flag
    for c in range(C):
        if flag2:
            print('*', end='')
        else:
            print('.', end='')
        flag2 = not flag2
    print()
    flag = not flag