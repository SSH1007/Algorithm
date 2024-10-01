import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    W, H, N = map(int, input().split())
    if N % 2:
        print((N - 1) / N * (N // 2) * H)
    else:
        print(H * ((N - 1) // 2))


if __name__ == '__main__':
    main()