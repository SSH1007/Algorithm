'''
1 1 1 
3 2 2
7 5 5
17 12 12
41 29 29
99 70 70
'''

# 2*N 배열 형태의 우리가 텅 비었을 때, 왼쪽만 있을 때, 오른쪽만 있을 때의 3케이스만 존재
# 우리의 세로 길이 N을 받는다.
N = int(input())
# dp 배열 초기화
dp = [[0]*3 for _ in range(N+1)]
# 2*1 우리의 경우를 우선 입력 (텅 빈거, 왼쪽, 오른쪽)
for i in range(3):
    dp[1][i] = 1
# 2부터 N까지 반복    
for i in range(2,N+1):
    # 위의 예시에서 도출한 점화식대로 계산
    dp[i][0] = (dp[i-1][0])%9901+(dp[i-1][1])%9901*2
    dp[i][1] = (dp[i-1][0])%9901+(dp[i-1][1])%9901
    dp[i][2] = (dp[i-1][0])%9901+(dp[i-1][1])%9901
# 출력
print(sum(dp[N])%9901)