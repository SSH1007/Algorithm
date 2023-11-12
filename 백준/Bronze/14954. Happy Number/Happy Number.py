N = input()
while 1:
    tmp = 0
    for n in N:
        tmp += int(n)**2
    N = str(tmp)
    if tmp == 1:
        print('HAPPY')
        break
    elif tmp == 4:
        print('UNHAPPY')
        break