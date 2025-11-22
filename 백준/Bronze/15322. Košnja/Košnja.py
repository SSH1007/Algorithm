import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    K = int(input())
    for _ in range(K):
        N, M = map(int, input().split())
        if N == 1 or M == 1:
            print(0)
        else:
            print((min(N, M)-2)*2+2)


if __name__ == '__main__':
    main()