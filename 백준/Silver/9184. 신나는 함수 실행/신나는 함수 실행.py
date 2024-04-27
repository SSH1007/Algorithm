import sys
input = sys.stdin.readline
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]


def W(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return W(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = W(a, b, c-1) + W(a, b-1, c-1) - W(a, b-1, c)
    else:
        dp[a][b][c] = W(a-1, b, c) + W(a-1, b-1, c) + W(a-1, b, c-1) - W(a-1, b-1, c-1)
    return dp[a][b][c]


while 1:
    a, b, c = map(int, input().rstrip().split())
    if a == b == c == -1:
        break
    print(f'w(%d, %d, %d) = %d' % (a, b, c, W(a, b, c)))