T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    cand = [0]*N
    for _ in range(M):
        Ns = list(map(int, input().split()))
        for n in range(N):
            cand[n] += Ns[n]
    print(cand.index(max(cand))+1)