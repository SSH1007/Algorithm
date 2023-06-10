import sys
input = sys.stdin.readline
m = int(input().rstrip())
n = int(input().rstrip())
if m<=2 or n<=2:
    print(m*n)
else:
    print(m*2+(n-2)*2)