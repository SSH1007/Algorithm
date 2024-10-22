import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = input()
    B = input()
    aL, bL = len(A), len(B)
    dp = [[''] * (bL+1) for _ in range(aL+1)]
    for i in range(1, aL+1):
        for j in range(1, bL+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + A[i-1]
            else:
                if len(dp[i-1][j]) > len(dp[i][j]):
                    dp[i][j] = dp[i-1][j]
                if len(dp[i][j-1]) > len(dp[i][j]):
                    dp[i][j] = dp[i][j-1]

    dap = dp[aL][bL]
    print(len(dap))
    if len(dap) > 0:
        print(dap)


if __name__ == '__main__':
    main()