N = int(input())
point = []
for _ in range(N):
    a,b = map(int, input().split())
    point.append((a,b))
point.sort(key=lambda i:(i[0], i[1]))
for p in point:
    print(p[0], p[1])