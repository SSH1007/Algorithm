import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, C = map(int, input().split())
    # 세로가 A, 가로가 B
    A, B = N, N
    for _ in range(C):
        X, Y = map(int, input().split())
        if X >= A or Y >= B:
            continue
        # 가로
        horizonCut = X*B
        # 세로
        verticalCut = Y*A
        if horizonCut >= verticalCut:
            A = X
        else:
            B = Y
    print(A*B)


if __name__ == '__main__':
    main()