import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = input().rstrip()
for n in range(1, N):
    if S[n] == 'J':
        print(S[n-1])