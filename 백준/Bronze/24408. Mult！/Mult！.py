import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    d, n = lst[0], 1
    while n < N:
        if lst[n] % d == 0:
            print(lst[n])
            n += 1
            d = lst[n]
        n += 1


if __name__ == '__main__':
    main()