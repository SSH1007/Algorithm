import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = int(input())
    print((N-1)*(M-1)*2)


if __name__ == '__main__':
    main()