D, K = map(int, input().split())
# 첫날에 준 떡의 개수 A, 둘째날에 준 떡의 개수 B
A, B = 1, 1
# 1일 2 = 2
# 2일 7 = 7
# 3일 9 = (2*1)+(7*1)
# 4일 16 = (2*1)+(7*2)
# 5일 25 = (2*2)+(7*3)
# 6일 41 = (2*3)+(7*5)
# 7일 66 = (2*5)+(7*8)

dp = ['']*(D+1)
dp[0] = 'a'
dp[1] = 'b'
for i in range(2, D):
    dp[i] = dp[i-1] + dp[i-2]
a = dp[D-1].count('a')
b = dp[D-1].count('b')
while A <= B:
    B = (-1*A*a + K)/b
    if B%1 == 0:
        print(A, int(B), sep='\n')
        break
    A += 1