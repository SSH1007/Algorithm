L = (10**6)+3002
prime = [0]*L
prime[0], prime[1] = 1, 1
for i in range(2, L):
    if prime[i] == 0:
        for j in range(i+i, L, i):
            prime[j] = 1
lst = []
for i in range(2, L):
    if not prime[i] and str(i) == str(i)[::-1]:
        lst.append(i)

N = int(input())
for l in lst:
    if l >= N:
        print(l)
        break