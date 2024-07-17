cipher = input()
# 암호가 잘못되어 해석할 수 없는 경우
if cipher[0] == '0':
    print(0)
    exit(0)
# dp에 맞추기 위해 암호 앞에 공백을 추가
cipher = ' ' + cipher
L = len(cipher)

dp = [0]*L
dp[0], dp[1] = 1, 1
for i in range(2, L):
    # 암호는 1부터
    if int(cipher[i]) > 0:
        dp[i] += dp[i-1]

    # 알파벳은 26(=십의 자리)까지이므로 해당 부분이 다른 해석이 가능한지를 판별
    if 10 <= int(cipher[i-1]+cipher[i]) <= 26:
        dp[i] += dp[i-2]

print(dp[-1] % 1000000)