import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    print('DIMI' if M <= sum(As)-N else 'OUT')


if __name__ == '__main__':
    main()