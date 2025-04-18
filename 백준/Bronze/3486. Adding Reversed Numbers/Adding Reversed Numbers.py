import sys
input = lambda: sys.stdin.readline().rstrip()


def F(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res


def main():
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        tmp = F(A) + F(B)
        print(F(tmp))


if __name__ == '__main__':
    main()