import sys
input = sys.stdin.readline
T = int(input().rstrip())
for t in range(1, T+1):
    a, b, c, d, e = input().rstrip().split()
    if b == '+':
        if int(a)+int(c) == int(e):
            print(f'Case {t}: YES')
        else:
            print(f'Case {t}: NO')
    else:
        if int(a)-int(c) == int(e):
            print(f'Case {t}: YES')
        else:
            print(f'Case {t}: NO')