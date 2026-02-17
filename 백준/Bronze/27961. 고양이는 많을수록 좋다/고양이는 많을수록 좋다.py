import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    d, c = 1, 1
    while d < N:
        d *= 2
        c += 1
    print(c)


if __name__ == '__main__':
    main()