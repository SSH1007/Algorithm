import sys
input = lambda: sys.stdin.readline().rstrip()


def F(i, d):
    if d == 1:
        c = ord(i[0])-64
        r = int(i[1])
    else:
        c = i % 8
        r = i//8 + (1 if i % 8 else 0)
    if c % 2 == r % 2:
        return 'B'
    else:
        return 'W'


def main():
    for _ in range(int(input())):
        O, T = input().split()
        T = int(T)
        if F(O, 1) == F(T, 2):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()