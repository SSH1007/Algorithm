L = int(input())
D = int(input())
X = int(input())
N, M = 10000, 0
for i in range(L, D+1):
    if sum(list(map(int, str(i)))) == X:
        N = min(N, i)
        M = max(M, i)
print(N, M, sep='\n')