import sys
input =  sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    i, f = map(int, input().rstrip().split())
    if i<=1 and f<=2:
        print('Yes')
    elif i<=2 and f<=1:
        print('Yes')
    else:
        print('No')