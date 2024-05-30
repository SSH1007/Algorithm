import sys
input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())
fix = []
for _ in range(M):
    fix.append(int(input().rstrip()))
# 테스트 결과, 문제 규칙대로의 좌석 구성 가지수는 피보나치 수열과 같음
dp = [0]*(41)
dp[0], dp[1], dp[2] = 1, 1, 2
for i in range(3, N+1):
    dp[i] = dp[i-2] + dp[i-1]
if M > 0:
    dap = 1
    dap *= dp[fix[0]-1]
    for i in range(1, M):
        dap *= dp[fix[i]-fix[i-1]-1]
    dap *= dp[N-fix[-1]]
else:
    dap = dp[N]
print(dap)