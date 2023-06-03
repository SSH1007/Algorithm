import sys
input = sys.stdin.readline
g, p, t = map(int, input().rstrip().split())
a = g*p
b = g + p*t
if a<b:
    print(1)
elif a>b:
    print(2)
else:
    print(0)