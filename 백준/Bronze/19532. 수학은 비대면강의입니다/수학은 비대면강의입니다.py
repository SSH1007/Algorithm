a, b, c, d, e, f = map(int, input().split())
status = 0
for x in range(-999,1000):
    for y in range(-999, 1000):
        if a*x+b*y==c and d*x+e*y==f:
            status = 1
            break
    if status:
        break
print(x, y)