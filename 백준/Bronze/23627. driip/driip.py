import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    if len(S) >= 5 and S[-5:] == 'driip':
        print('cute')
    else:
        print('not cute')


if __name__ == '__main__':
    main()