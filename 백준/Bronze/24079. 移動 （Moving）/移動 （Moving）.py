import sys
input = sys.stdin.readline
x = int(input().rstrip())
y = int(input().rstrip())
z = int(input().rstrip())
print(1 if (x+y)*60 < z*60+30 else 0)