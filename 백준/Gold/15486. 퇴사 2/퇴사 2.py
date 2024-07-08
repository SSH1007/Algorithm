import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    T, P = [0]*(N+1), [0]*(N+1)
    for n in range(1, N+1):
        t, p = map(int, input().split())
        T[n] = t
        P[n] = p
    dp = [0]*(N+1)
    # dp[d] = d일차의 최대 이익
    # T[d]가 1이면 d일 근무를 마치면 바로 이익을 얻을 수 있다
    for d in range(1, N+1):
        dp[d] = max(dp[d-1], dp[d])
        finish_d = d+T[d]-1
        # d일부터 T[d]일만큼 더 일한 결과(당일 포함), 퇴사일인 N을 초과할 경우 continue
        if finish_d > N:
            continue
        dp[finish_d] = max(dp[d-1]+P[d], dp[finish_d])
    print(max(dp))


if __name__ == '__main__':
    main()