import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    n, m = map(int, input().rstrip().split())
    reds = list(map(int, input().rstrip().split()))
    whites = list(map(int, input().rstrip().split()))
    if len(reds) > len(whites):
        print('No')
    else:
        print('Yes')