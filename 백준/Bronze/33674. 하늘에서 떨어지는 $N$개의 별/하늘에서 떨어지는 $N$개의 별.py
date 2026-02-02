import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, D, K = map(int, input().split())
    lst = list(map(int, input().split()))
    S = K//max(lst)
    print((D-1)//S)


if __name__ == '__main__':
    main()