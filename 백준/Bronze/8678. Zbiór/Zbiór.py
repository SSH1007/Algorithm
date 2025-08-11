import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    z = int(input())
    for _ in range(z):
        a, b = map(int, input().split())
        if b % a == 0:
            print('TAK')
        else:
            print('NIE')


if __name__ == '__main__':
    main()