import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B, C = map(int, input().split())
    if C % 2 == 0:
        print(A)
    else:
        print(A^B)


if __name__ == '__main__':
    main()