def fun():
    #          (M - 1)열    M열
    # (N - 2)행     1        2
    # (N - 1)행     3        4
    #       N행     5        6
    #
    #           (K - 2)열 (K - 1)열  K열
    # (M - 1)행   - 1        - 2      0
    #       M행     0          0      3

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    M, K = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(M)]

    C = [[0 for _ in range(K)] for _ in range(N)]

    for n in range(N):
        for k in range(K):
            for m in range(M):
                C[n][k] += A[n][m]*B[m][k]

    for c in C:
        print(*c)

if __name__ == '__main__':
    fun()