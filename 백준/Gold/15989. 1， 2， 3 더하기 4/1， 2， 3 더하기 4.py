import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    # 모두 1로만 표현할 수 있는 경우의 수 하나쯤은 갖고 있으므로 1로 초기화
    dp = [1]*10001
    for i in range(2, 10001):
        dp[i] += dp[i-2]
    for i in range(3, 10001):
        dp[i] += dp[i-3]
    for _ in range(T):
        n = int(input())
        print(dp[n])


if __name__ == '__main__':
    main()