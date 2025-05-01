import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, C = map(int, input().split())
    # 세로가 A, 가로가 B
    A, B = N, N
    for _ in range(C):
        X, Y = map(int, input().split())
        # 가로
        horizonCut = (0 if X >= A else X)*B
        # 세로
        verticalCut = (0 if Y >= B else Y)*A
        if horizonCut >= verticalCut:
            A = X
        else:
            B = Y
    print(A*B)


if __name__ == '__main__':
    main()