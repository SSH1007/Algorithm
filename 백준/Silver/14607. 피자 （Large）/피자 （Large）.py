import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    print(N*(N-1)//2)


if __name__ == '__main__':
    main()