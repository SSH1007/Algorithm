import sys
input = sys.stdin.readline
S = list(input().rstrip())
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
S.sort()
for i in range(25):
    if S[i] != abc[i]:
        print(abc[i])
        break
else:
    print('Z')