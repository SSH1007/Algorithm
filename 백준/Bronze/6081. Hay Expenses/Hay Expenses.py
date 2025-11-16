import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, Q = map(int, input().split())
    H = [int(input()) for _ in range(N)]
    P = [list(map(int, input().split())) for _ in range(Q)]
    for p in P:
        print(sum(H[p[0]-1:p[1]]))


if __name__ == '__main__':
    main()