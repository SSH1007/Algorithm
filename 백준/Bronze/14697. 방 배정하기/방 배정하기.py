# bottom-up 방식 DP 
A, B, C, N = map(int, input().split())
# 전체 학생 수 300에 맞춰 초기화
dp = [0]*(300+1)
# 일단 N이 A명이나 B명, 혹은 C명일 경우 무조건 가능(1)
dp[A]=dp[B]=dp[C]=1
# A명부터 N까지 순회
for i in range(A,N+1):
    # 순회하고 있는 현재 수보다 A or B or C만큼 작은 수는 무조건 가능(1)
    for j in [A, B, C]:
        if i>=j and dp[i-j]:
            dp[i]=1
print(dp[N])