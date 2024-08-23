import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    # dp[i][n] = i번째 책상의 n번째 점수
    dp = [[0]*6 for _ in range(N+1)]
    cnt, grade = 0, 6
    for i in range(1, N+1):
        A, B = map(int, input().split())
        dp[i][A] = dp[i-1][A] + 1
        if dp[i][A] > cnt:
            cnt = dp[i][A]
        if A != B:
            dp[i][B] = dp[i-1][B] + 1
            if dp[i][B] > cnt:
                cnt = dp[i][B]
    for i in range(1, N+1):
        for j in range(1, 6):
            if dp[i][j] == cnt:
                grade = min(grade, j)
    print(cnt, grade)


if __name__ == '__main__':
    main()