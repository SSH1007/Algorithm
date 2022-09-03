N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins = [x for x in coins if K>=x]
coins.sort(reverse=True)
cnt = 0

for c in coins:
    cnt+=(K//c)
    K%=c
print(cnt)