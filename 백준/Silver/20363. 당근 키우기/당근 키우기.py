import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X, Y = map(int, input().split())
    print(X+Y+X//10 if X < Y else X+Y+Y//10)


if __name__ == '__main__':
    main()