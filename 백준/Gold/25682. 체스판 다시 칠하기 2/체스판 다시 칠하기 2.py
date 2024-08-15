import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M, K = map(int, input().split())
    pan = [list(input()) for _ in range(N)]

    # 맨 왼쪽 위 칸이 하얀 체스판의 누적합 값
    s_white = [[0]*(M+1) for _ in range(N+1)]
    # 맨 왼쪽 위 칸이 검은 체스판의 누적합 값
    s_black = [[0]*(M+1) for _ in range(N+1)]

    for n in range(N):
        for m in range(M):
            if (n+m) % 2 == 0:
                if pan[n][m] == 'B':
                    s_white[n+1][m+1] = 1
                else:
                    s_black[n+1][m+1] = 1
            else:
                if pan[n][m] == 'B':
                    s_black[n+1][m+1] = 1
                else:
                    s_white[n+1][m+1] = 1

    for n in range(1, N+1):
        for m in range(1, M+1):
            s_white[n][m] = s_white[n][m] + s_white[n-1][m] + s_white[n][m-1] - s_white[n-1][m-1]
            s_black[n][m] = s_black[n][m] + s_black[n-1][m] + s_black[n][m-1] - s_black[n-1][m-1]


    w_min, b_min = 4000000, 4000000
    for n in range(K, N+1):
        for m in range(K, M+1):
            part_w = s_white[n][m] + s_white[n-K][m-K] - s_white[n-K][m] - s_white[n][m-K]
            w_min = min(w_min, part_w)
            part_b = s_black[n][m] + s_black[n-K][m-K] - s_black[n-K][m] - s_black[n][m-K]
            b_min = min(b_min, part_b)
    print(min(w_min, b_min))


if __name__ == '__main__':
    main()