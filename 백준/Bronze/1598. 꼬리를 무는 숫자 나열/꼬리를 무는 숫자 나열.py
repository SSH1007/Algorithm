import math
a, b = map(int, input().split())
ax = math.ceil(a/4)
if a%4 == 0:
    ay = 4
else:
    ay = a%4
bx = math.ceil(b/4)
if b%4 == 0:
    by = 4
else:
    by = b%4

print(abs(ax-bx)+abs(ay-by))