import sys
sys.setrecursionlimit(10**6)


def Cantor(line, idx):
    l = len(line)
    if l == 3 and idx != 1:
        return '- -'
    elif l >= 3 and idx == 1:
        return line.replace('-', ' ')
    tmp = []
    for i in range(0, l, l//3):
        tmp.append(line[i:i+l//3])
    return Cantor(tmp[0], 0) + Cantor(tmp[1], 1) + Cantor(tmp[2], 2)


while 1:
    try:
        N = input()
        if N == '':
            break
        N = int(N)
        line = '-'*(3**N)
        if N == 0:
            print('-')
        else:
            print(Cantor(line, 0))
    except EOFError:
        break