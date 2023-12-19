def isprime(n):
    prime = True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            prime = False
            break
    return prime


import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    if n < 3:
        print(2)
    else:
        while 1:
            if isprime(n):
                print(n)
                break
            else:
                n += 1