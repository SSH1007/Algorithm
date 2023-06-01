import sys
input = sys.stdin.readline
S = input().rstrip()
print('YES' if int(S[0])+int(S[4])==int(S[8]) else 'NO')