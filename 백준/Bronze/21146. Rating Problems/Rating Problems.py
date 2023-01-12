n, k = map(int, input().split())
lst = []
for _ in range(k):
    lst.append(int(input()))
forMax = 3*(n-k)
forMin = -3*(n-k)
print((sum(lst)+forMin)/n, (sum(lst)+forMax)/n)