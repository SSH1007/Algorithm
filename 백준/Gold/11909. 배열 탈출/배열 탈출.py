import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    inf = float('inf')
    dp = [[inf]*N for _ in range(N)]
    dp[0][0] = 0
    for r in range(N):
        for c in range(N):
            if r+1 < N:
                tmp = dp[r][c] + (0 if maps[r][c] > maps[r+1][c] else maps[r+1][c]-maps[r][c]+1)
                if dp[r+1][c] > tmp:
                    dp[r+1][c] = tmp
            if c+1 < N:
                tmp = dp[r][c] + (0 if maps[r][c] > maps[r][c+1] else maps[r][c+1]-maps[r][c]+1)
                if dp[r][c+1] > tmp:
                    dp[r][c+1] = tmp
    print(dp[N-1][N-1])


if __name__ == '__main__':
    main()