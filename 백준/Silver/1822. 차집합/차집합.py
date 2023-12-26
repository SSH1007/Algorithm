n, m = map(int, input().split())
a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
c = a.difference(b)
if c:
    print(len(c))
    print(*sorted(list(c)))
else:
    print(0)