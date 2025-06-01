import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    if 'ss' in N:
        print('hiss')
    else:
        print('no hiss')


if __name__ == '__main__':
    main()