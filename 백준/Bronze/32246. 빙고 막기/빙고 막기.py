import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N == 2:
        print(3)
    else:
        print(N)


if __name__ == '__main__':
    main()