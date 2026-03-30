t = int(input())
for _ in range(t):
    S = input()
    if (int(S[:2])**2+int(S[2:])**2)%7 == 1:
        print('YES')
    else:
        print('NO')