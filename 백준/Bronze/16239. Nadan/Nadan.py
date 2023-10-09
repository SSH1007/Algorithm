K = int(input())
N = int(input())
hap = 0
for k in range(1, N):
    print(k)
    hap += k
print(K-hap)