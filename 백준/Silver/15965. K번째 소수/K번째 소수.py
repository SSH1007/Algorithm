K = int(input())
MAX = 10**7
prime = [0]*MAX
for i in range(2, MAX):
    if not prime[i]:
        for j in range(i+i, MAX, i):
            prime[j] = 1
cnt = 0
for k in range(2, MAX):
    if not prime[k]:
        cnt += 1
    if cnt == K:
        print(k)
        break