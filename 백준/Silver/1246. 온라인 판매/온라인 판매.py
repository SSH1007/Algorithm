N, M = map(int, input().split())
prices = [int(input()) for _ in range(M)]
prices.sort()
price = 0
revenue = 0
for p in prices:
    egg = min(M, N)
    if p*egg >= revenue:
        revenue = p*egg
        price = p
    M -= 1
print(price, revenue)