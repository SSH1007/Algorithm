# 9251번 : 최장 공통 부분 수열(LCS)
import sys
input = sys.stdin.readline


def main():
    A = input().rstrip()
    B = input().rstrip()
    aL, bL = len(A), len(B)
    dp = [[0]*(aL+1) for _ in range(bL+1)]

    for b in range(1, bL+1):
        for a in range(1, aL+1):
            if A[a-1] == B[b-1]:
                dp[b][a] = dp[b-1][a-1]+1
            else:
                dp[b][a] = max(dp[b-1][a], dp[b][a-1])

    print(dp[bL][aL])
    return


if __name__ == '__main__':
    main()