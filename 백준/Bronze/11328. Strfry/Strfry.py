import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    a, b = input().rstrip().split()
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')