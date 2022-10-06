def perm(K,N,M,L):
    if K==M:
        print(*res)
        return
    else:
        for n in range(N):
            if not visited[n] and L<arr[n]:
                visited[n] = True
                L = arr[n]
                res[K] = arr[n]
                perm(K+1,N,M,L)
                visited[n] = False

# N개의 숫자 중에서 M개를 선택한다.
N, M = map(int, input().split())
# 1부터 N까지의 N개의 숫자
arr = range(1,N+1)
# 선택된 숫자 모음
res = [0]*M
# 선택 완료 여부 모음(중복없이 고르기 위함)
visited = [False]*N 
perm(0, N, M, 0)