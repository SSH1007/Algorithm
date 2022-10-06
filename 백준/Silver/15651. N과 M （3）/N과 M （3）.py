def perm(K,N,M):
    if K==M:
        print(*res)
        return
    else:
        for n in range(N):
            res[K] = arr[n]
            perm(K+1,N,M)

# N개의 숫자 중에서 M개를 선택한다.
N, M = map(int, input().split())
# 1부터 N까지의 N개의 숫자
arr = range(1,N+1)
# 선택된 숫자 모음
res = [0]*M
perm(0, N, M)