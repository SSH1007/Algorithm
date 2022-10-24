a, b = map(int, input().split())
n = int(input())
for _ in range(n):
    c = int(input())
    if c <= 1000:
        print(c, c*a)
    else:
        print(c, 1000*a+(c-1000)*b)