import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B = map(int, input().split())
    if A > B:
        print(B+B+1)
    else:
        print(A+A-1)


if __name__ == '__main__':
    main()