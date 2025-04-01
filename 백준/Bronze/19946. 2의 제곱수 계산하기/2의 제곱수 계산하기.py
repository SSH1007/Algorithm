import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    cnt = 0
    while N > 0:
        if N & 1:
            cnt += 1
        N >>= 1
    print(cnt)


if __name__ == '__main__':
    main()