import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    x, k, a = map(int, input().split())
    print(0 if x % (k+a) >= k else 1)


if __name__ == '__main__':
    main()