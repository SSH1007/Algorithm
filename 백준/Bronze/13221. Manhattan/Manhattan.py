X, Y = map(int, input().split())
n = int(input())
m = 201
x, y = X, Y
for _ in range(n):
    a, b = map(int, input().split())
    if abs(a-X)+abs(b-Y) < m:
        m = abs(a-X)+abs(b-Y)
        x, y = a, b
print(x, y)