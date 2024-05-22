import sys
input = sys.stdin.readline
N = int(input().rstrip())
BOJ = input().rstrip()
inf = int(1e9)
dp = [inf]*N
dp[0] = 0


def f():
    for i in range(N):
        for j in range(i+1, N):
            if BOJ[i] == 'B' and not BOJ[j] == 'O':
                continue
            if BOJ[i] == 'O' and not BOJ[j] == 'J':
                continue
            if BOJ[i] == 'J' and not BOJ[j] == 'B':
                continue
            dp[j] = min(dp[j], dp[i]+(j-i)**2)
    if dp[N-1] == inf:
        print(-1)
    else:
        print(dp[N-1])


f()