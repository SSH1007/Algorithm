T = int(input())
a, b = 0, 0
for _ in range(T):
    x, y = map(int, input().split())
    if x > y:
        a += (x+y)
    elif x < y:
        b += (x+y)
    else:
        a += x
        b += y
print(a, b)