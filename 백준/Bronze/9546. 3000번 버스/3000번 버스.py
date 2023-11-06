T = int(input())
for _ in range(T):
    k = int(input())
    p = 0
    for _ in range(k):
        p += 0.5
        p *= 2
    print(int(p))