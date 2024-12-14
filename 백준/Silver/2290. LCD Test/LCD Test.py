import sys
input = lambda: sys.stdin.readline().rstrip()

s, n = map(int, input().split())
h, v = '-', '|'


def num(x):
    maps = [[' ']*(s+2) for _ in range(2*s+3)]
    if x == 0:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][0] = '|'
            maps[i][s+1] = '|'
            maps[i+s+1][0] = '|'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    elif x == 1:
        for i in range(1, s+1):
            maps[i][s+1] = '|'
            maps[i+s+1][s+1] = '|'
    elif x == 2:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][s+1] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][0] = '|'
            maps[2*s+2][i] = '-'
    elif x == 3:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][s+1] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    elif x == 4:
        for i in range(1, s+1):
            maps[i][0] = '|'
            maps[i][s+1] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][s+1] = '|'
    elif x == 5:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][0] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    elif x == 6:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][0] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][0] = '|'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    elif x == 7:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][s+1] = '|'
            maps[i+s+1][s+1] = '|'
    elif x == 8:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][0] = '|'
            maps[i][s+1] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][0] = '|'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    elif x == 9:
        for i in range(1, s+1):
            maps[0][i] = '-'
            maps[i][0] = '|'
            maps[i][s+1] = '|'
            maps[s+1][i] = '-'
            maps[i+s+1][s+1] = '|'
            maps[2*s+2][i] = '-'
    return maps


dap = []
for nn in str(n):
    dap.append(num(int(nn)))

ans = list(zip(*dap))
for an in ans:
    for a in an:
        print(''.join(a), end=' ')
    print()