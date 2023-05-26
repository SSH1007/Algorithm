import sys
input = sys.stdin.readline
X, Y = map(int, input().rstrip().split())
a = 100-X
b = 100-Y
c = 100 - (a+b)
d = a*b
q = d//100
r = d%100
print(a, b, c, d, q, r)
print(c+q, r)