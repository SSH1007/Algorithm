# dp O(N^2)이므로 1000 이하에서 유효
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    As = list(map(int, input().split()))
    dp = [1]*N     # dp[i]는 As[i]를 마지막으로 하는 LIS의 길이
    prev = [-1]*N  # 역추적용. LIS의 이전 원소의 인덱스 기록

    for i in range(1, N):
        for j in range(i):
            if As[j] < As[i] and dp[i] < dp[j]+1:
                dp[i] = dp[j]+1
                prev[i] = j

    restore = []
    # LIS 마지막 원소의 인덱스부터 역순으로 추적
    idx = dp.index(max(dp))
    while idx != -1:
        restore.append(As[idx])
        idx = prev[idx]
    print(len(restore))
    print(*restore[::-1])


if __name__ == '__main__':
    main()