import sys
input = sys.stdin.readline
N = int(input().rstrip())
if N==0:
    print(1)
elif N == 1:
    print(0)
else:
    print(N%2*'4',end='')
    print(N//2*'8')