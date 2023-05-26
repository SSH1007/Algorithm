import sys
input = sys.stdin.readline
A1 = int(input().rstrip())
A2 = int(input().rstrip())
A3 = int(input().rstrip())
min1 = A2*2 + A3*4
min2 = A1*2 + A3*2
min3 = A1*4 + A2*2
print(min(min1, min2, min3))