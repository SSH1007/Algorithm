import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    if n%2 == m%2 == 1:
        print(n*m-1)
    else:
        print(n*m)


if __name__ == '__main__':
    main()