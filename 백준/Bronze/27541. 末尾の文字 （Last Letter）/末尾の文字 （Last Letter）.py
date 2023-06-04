import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = input().rstrip()
if S[-1] == 'G':
    print(S[:-1])
else:
    print(S+'G')