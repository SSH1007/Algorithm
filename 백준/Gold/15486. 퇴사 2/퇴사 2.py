import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
T, P = [0]*(N+2), [0]*(N+2)
for n in range(1, N+1):
    t, p = map(int, input().split())
    T[n] = t
    P[n] = p
# print(T)
# print(P)
dp = [0]*(N+2)
max_v = 0
for d in range(1, N+2):
    max_v = max(max_v, dp[d])
    finish_d = d+T[d]-1
    # d일부터 T[d]일만큼 더 일한 결과, 퇴사일인 N을 초과할 경우 continue
    if finish_d > N:
        continue
    # print(d, finish_d+1, max_v, P[d], dp[finish_d])
    dp[finish_d+1] = max(max_v+P[d], dp[finish_d+1])
print(max(dp))