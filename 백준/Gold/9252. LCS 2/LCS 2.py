import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    A = input()
    B = input()
    al, bl = len(A), len(B)
    dp = [[0]*(bl+1) for _ in range(al+1)]
    for i in range(1, al+1):
        for j in range(1, bl+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j])
                dp[i][j] = max(dp[i][j-1], dp[i][j])

    L = dp[al][bl]
    print(L)
    if L == 0:
        exit(0)
    # 역추적
    r, c = al, bl
    lst = []
    while r > 0 and c > 0:
        if dp[r-1][c] == dp[r][c]:
            r -= 1
        elif dp[r][c-1] == dp[r][c]:
            c -= 1
        else:
            lst.append(A[r-1])
            r -= 1
            c -= 1
    print(''.join(lst)[::-1])


if __name__ == '__main__':
    main()