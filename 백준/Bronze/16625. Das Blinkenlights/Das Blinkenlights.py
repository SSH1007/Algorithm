import sys
input = lambda: sys.stdin.readline().rstrip()


def F(a, b):
    while b > 0:
        a, b = b, a%b
    return a


def main():
    p, q, s = map(int, input().split())
    print('yes' if p*q//F(p, q) <= s else 'no')


if __name__ == '__main__':
    main()