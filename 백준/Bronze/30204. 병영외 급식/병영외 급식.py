import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, X = map(int, input().split())
    Ps = list(map(int, input().split()))
    if sum(Ps) % X:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()