# 문자열의 길이, 문제의 수가 각각 200,000이므로 O(n)인 count는 시간 초과...
# 따라서 누적합으로 시간복잡도 줄이기
import sys
input = sys.stdin.readline


def f():
    S = input().rstrip()
    q = int(input().rstrip())
    L = len(S)
    dp = [[0]*(L+1) for _ in range(26)]
    for j in range(L):
        dp[ord(S[j])-97][j] = 1
    for i in range(26):
        for j in range(1, L):
            dp[i][j] = dp[i][j] + dp[i][j-1]

    for _ in range(q):
        a, l, r = input().rstrip().split()
        l, r = int(l), int(r)
        print(dp[ord(a)-97][r]-dp[ord(a)-97][l-1])


f()