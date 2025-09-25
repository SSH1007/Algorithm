import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, P, C = map(int, input().split())
    p = A+C
    print(p if p > P else P)


if __name__ == '__main__':
    main()