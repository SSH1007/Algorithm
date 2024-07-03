import sys
input = sys.stdin.readline


def main():
    # 남아있는 모든 전깃줄이 서로 교차하지 않기 위해 없애야 하는 최소 개수 구하기
    # => 남아있는 모든 전깃줄이 서로 교차하지 않는 최대 개수 구헤서 전체에서 빼면 된다.
    N = int(input().rstrip())
    info = [list(map(int, input().rstrip().split())) for _ in range(N)]
    # A전봇대 기준으로 B전봇대 정렬
    info.sort(key=lambda x: x[0])
    dp = [0]*N
    # dp[i] = i번째 수가 마지막 수인 부분수열의 최장 길이
    for i in range(N):
        # 부분수열의 길이의 최솟값은 언제나 1
        dp[i] = 1
        for j in range(i):
            if info[i][1] > info[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    print(N-max(dp))


if __name__ == '__main__':
    main()