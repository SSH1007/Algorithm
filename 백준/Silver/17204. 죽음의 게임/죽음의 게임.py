import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    As = [int(input()) for _ in range(N)]
    n, cnt = 0, 1
    for _ in range(N):
        n = As[n]
        if n == K:
            print(cnt)
            exit(0)
        cnt += 1
    print(-1)


if __name__ == '__main__':
    main()