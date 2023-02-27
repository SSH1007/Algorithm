N, M = map(int, input().split())
baskets = [0]*N
for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i,j+1):
        baskets[x-1] = k
print(*baskets)