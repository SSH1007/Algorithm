import sys
input = sys.stdin.readline
A = int(input().rstrip())
B = int(input().rstrip())
if A+B*7 > 30:
    print(0)
else:
    print(1)