import sys
input = sys.stdin.readline
A = int(input().rstrip())
B = int(input().rstrip())
print(12 if (A+B)%12 == 0 else (A+B)%12)