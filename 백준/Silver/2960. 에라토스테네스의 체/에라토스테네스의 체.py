N, K = map(int, input().split())

cnt = 0
lst = [i for i in range(N+1)]

for n in range(2, N+1):
    for i in range(n, N+1, n):
        if lst[i]:
            cnt += 1
            if cnt == K:
                print(i)
                exit(0)
            lst[i] = 0