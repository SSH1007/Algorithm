import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    mx = 1
    while n != 1:
        mx = max(mx, n)
        if n % 2:
            n *= 3
            n += 1
        else:
            n //= 2
    print(mx)