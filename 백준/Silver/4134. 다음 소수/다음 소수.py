def isprime(n):
    if n <= 1 or n%2 == 0:
        if n == 2:
            return True
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True


import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    while not isprime(n):
        n += 1
    print(n)