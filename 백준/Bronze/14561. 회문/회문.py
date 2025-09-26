import sys
input = lambda: sys.stdin.readline().rstrip()


def F(A, n):
    hex = '0123456789ABCDEF'
    res = []
    while A > 0:
        A, x = divmod(A, n)
        res.append(hex[x])
    if res == list(reversed(res)):
        return 1
    else:
        return 0


def main():
    T = int(input())
    for _ in range(T):
        A, n = map(int, input().split())
        print(F(A, n))


if __name__ == '__main__':
    main()