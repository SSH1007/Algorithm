import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b, c = input().split()
    if b == 'AND':
        if a == c == 'true':
            print('true')
        else:
            print('false')
    else:
        if a == 'true' or c == 'true':
            print('true')
        else:
            print('false')


if __name__ == '__main__':
    main()