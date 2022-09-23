N = int(input())
S = input()
cnt = 0
for i in range(N):
    if S[i] in ['a','i','u','e','o']:
        cnt+=1
print(cnt)