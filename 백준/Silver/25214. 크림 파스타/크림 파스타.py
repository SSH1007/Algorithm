import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    dp = [0]*N
    minV = As[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1], As[i]-minV)
        minV = min(minV, As[i])
    print(*dp)


if __name__ == '__main__':
    main()