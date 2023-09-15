N, M = map(int, input().split())
si = list(map(int, input().split()))
si.extend([0]*M)
for n in range(N):
    nm = list(map(int, input().split()))
    for i in range(N+M):
        si[n] -= nm[i]
        si[i] += nm[i]
print(*si)