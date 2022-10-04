def perm(K,N,M):
    if K==M:
        print(*res)
        return
    else:
        for n in range(N):
            if not visited[n]:
                visited[n] = True
                res[K] = arr[n]
                perm(K+1,N,M)
                visited[n] = False

N, M = map(int, input().split())
arr = range(1,N+1)
res = [0]*M
visited = [False]*N 
perm(0, N, M)