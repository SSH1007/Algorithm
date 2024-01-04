N, K = map(int, input().split())
l = (K+1)*K//2
if N < l:
    print(-1)
else:
    if (N-l)%K == 0:
        print(K-1)
    else:
        print(K)