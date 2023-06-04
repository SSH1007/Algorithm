import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = input().rstrip()
cnt = S.count('LL')
if cnt <= 1:
    print(N)
else:
    print(N-cnt+1)