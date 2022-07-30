N,M = map(int,input().split())
pod = list(range(1,N+1))
for m in range(M):
    i,j = map(int,input().split())
    rl = list(reversed(pod[i-1:j]))
    pod = pod[:i-1]+rl+pod[j:]
for p in pod:
    print(p,end = ' ')