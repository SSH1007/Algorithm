import sys
input = sys.stdin.readline
n = int(input().rstrip())
if n%2:
    print(0)
else:
    if (n//2)%2:
        print(1)
    else:
        print(2)