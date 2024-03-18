import sys
input = sys.stdin.readline
n = int(input().rstrip())
sack = []
for _ in range(n):
    a = list(map(int, input().rstrip().split()))
    if a[0] == 0:
        if sack:
            print(sack.pop())
        else:
            print(-1)
    else:
        sack.extend(a[1:])
        sack.sort()