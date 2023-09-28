S = input()
a = S[0]
cnt = 1
for i in range(1, len(S)):
    if S[i] != a:
        break
    cnt += 1
print(cnt)