import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = input()
    B = input()
    if A == 'null':
        print('NullPointerException')
        print('NullPointerException')
    else:
        print('true' if A == B else 'false')
        if B == 'null':
            print('false')
        else:
            print('true' if A.lower() == B.lower() else 'false')


if __name__ == '__main__':
    main()