N = input()
l = [str(N)]


def happy(N):
    if N == '1':
        print('HAPPY')
        return
    v = 0
    for n in N:
        v += int(n)**2
    if str(v) in l:
        print('UNHAPPY')
        return
    l.append(str(v))
    happy(str(v))


happy(N)