N = int(input())
alst = list(map(int, input().split()))
odd, even = 0, 0
for a in alst:
    if a%2:
        odd += 1
    else:
        even += 1
if N%2:
    if odd > even:
        print(1)
    else:
        print(0)
else:
    if odd == even:
        print(1)
    else:
        print(0)