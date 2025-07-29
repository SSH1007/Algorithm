import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = 1
    while 1:
        p, s = map(int, input().split())
        if p == 0:
            break
        print(f'Hole #{t}')
        if s == p:
            print('Par.')
        elif s == 1:
            print('Hole-in-one.')
        elif s == p-1:
            print('Birdie.')
        elif s == p-2:
            print('Eagle.')
        elif s == p-3:
            print('Double eagle.')
        elif s == p+1:
            print('Bogey.')
        else:
            print('Double Bogey.')
        print()
        t += 1


if __name__ == '__main__':
    main()