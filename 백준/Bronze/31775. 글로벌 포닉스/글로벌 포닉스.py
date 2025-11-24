import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    s = set()
    for _ in range(3):
        s.add(input()[0])
    if s == {'l', 'k', 'p'}:
        print('GLOBAL')
    else:
        print('PONIX')


if __name__ == '__main__':
    main()