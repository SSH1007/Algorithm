T = int(input())
limit = 1000001
ech = [1]*limit
prime = []
for i in range(2, limit):
    if ech[i]:
        prime.append(i)
        for j in range(i+i, limit, i):
            ech[j] = 0

for _ in range(T):
    N = int(input())
    dap = 0
    for p in prime:
        if p >= N:
            break
        if ech[N-p] and p <= N-p:
            dap += 1
    print(dap)