import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, m = map(int, input().split())
    x = 1
    while 1:
        if (a*x)%m == 1:
            break
        x += 1
    print(x)


if __name__ == '__main__':
    main()