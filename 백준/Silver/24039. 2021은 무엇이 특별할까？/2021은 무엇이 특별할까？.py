N = int(input())
lst = [0]*110
lst[0], lst[1] = 1, 1
for i in range(2, 110):
    if lst[i] == 0:
        for j in range(i+i, 110, i):
            lst[j] = 1
prime = [i for i in range(110) if not lst[i]]


def f(N):
    while 1:
        N += 1
        for i in range(len(prime)-1):
            if prime[i]*prime[i+1] == N:
                return N


print(f(N))