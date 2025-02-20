import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    C, K = map(int, input().split())
    t = C%(10**K)
    if t >= 10**K/2:
        C += 10**K
    C -= t
    print(C)


if __name__ == '__main__':
    main()