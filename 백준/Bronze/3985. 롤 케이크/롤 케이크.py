L = int(input())
N = int(input())
cake = [0]*(L+1)
audience = []
greed = 0
for n in range(1, N+1):
    p, k = map(int, input().split())
    ate = 0
    greed = k-p+1
    for i in range(p, k+1):
        if not cake[i]:
            cake[i] = n
            ate += 1
    audience.append((n, greed, ate))

audience.sort(key=lambda x: -x[1])
print(audience[0][0])
audience.sort(key=lambda x: (-x[2], x[0]))
print(audience[0][0])