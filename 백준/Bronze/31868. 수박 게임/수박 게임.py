import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    cnt = 1
    while 1:
        if cnt == N:
            print(K)
            break
        K //= 2
        cnt += 1


if __name__ == '__main__':
    main()