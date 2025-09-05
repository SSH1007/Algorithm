import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        if a*b > c*d:
            print('TelecomParisTech')
        elif a*b < c*d:
            print('Eurecom')
        else:
            print('Tie')


if __name__ == '__main__':
    main()