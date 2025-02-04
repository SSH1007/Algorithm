import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    Q = int(input())
    q = 0
    for _ in range(Q):
        a, b = map(int, input().split())
        if a%2:
            q += b
        else:
            q -= b
        if q < 0:
            print('Adios')
            return 0
    print('See you next month')


if __name__ == '__main__':
    main()