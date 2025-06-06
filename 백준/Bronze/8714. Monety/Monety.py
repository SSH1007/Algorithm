import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    c = lst.count(1)
    print(min(c, n-c))


if __name__ == '__main__':
    main()