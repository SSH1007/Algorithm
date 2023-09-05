button = list(map(int, input().split()))
don = 5000
for b in button:
    if b == 1:
        don -= 500
    elif b == 2:
        don -= 800
    elif b == 3:
        don -= 1000
print(don)