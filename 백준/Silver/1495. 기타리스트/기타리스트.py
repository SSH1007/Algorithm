import sys
input = sys.stdin.readline
# 곡의 개수 N, 시작 볼륨 S, 최대 볼륨 M
N, S, M = map(int, input().rstrip().split())
# v[i]는 i번째 곡을 연주하기 전에 바꿀 수 있는 볼륨(+-)
V = list(map(int, input().rstrip().split()))


def f():
    # 직접 그림을 그려보니 어떻게 2차원 dp를 구성해야 할지 감이 잡히는 케이스였다.
    dp = [[0]*(N+1) for _ in range(M+1)]
    dp[S][0] = 1

    for i in range(1, N+1):
        for j in range(M+1):
            if dp[j][i-1]:
                if j+V[i-1] <= M:
                    dp[j+V[i-1]][i] = 1
                if j-V[i-1] >= 0:
                    dp[j-V[i-1]][i] = 1

    for i in range(M, -1, -1):
        if dp[i][N] == 1:
            return i
    return -1


print(f())