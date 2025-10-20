import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A, B = map(int, input().split())
    while A != B:
        A, B = max(A, B) - min(A,B), min(A, B)
    print(B)


if __name__ == '__main__':
    main()