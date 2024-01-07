sieve = [1]*1000
sieve[0], sieve[1] = 0, 0
for i in range(1000):
    if sieve[i]:
        for j in range(i+i, 1000, i):
            sieve[j] = 0
lst = []
for i in range(1000):
    if sieve[i]:
        lst.append(i)

T = int(input())


def f(n):
    for i in lst:
        for j in lst:
            for k in lst:
                if i+j+k == n:
                    return [i, j, k]
    return []


for _ in range(T):
    n = int(input())
    dap = f(n)
    if dap:
        print(*dap)
    else:
        print(0)