import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for p in range(19, -1, -1):
        if N % (2**p) == 0:
            if (N // (2**p)) % 2:
                print(N // (2**p), p)
                return


if __name__ == '__main__':
    main()