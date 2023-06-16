# 3m 30s = 210s
K = int(input())
N = int(input())
time = 0
for _ in range(N):
    T, Z = input().split()
    T = int(T)
    time += T
    if time >= 210:
        print(K)
        break
    if Z == 'T':
        K += 1
        if K>8:
            K=1