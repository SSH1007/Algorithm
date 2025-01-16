import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    n, c = 0, 0
    while 1:
        n += 1
        c += 1
        if n == N:
            print(c)
            break
        if '50' in str(n):
            c += 1


if __name__ == '__main__':
    main()