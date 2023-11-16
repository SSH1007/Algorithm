N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

for inf in info:
    for _ in range(K):
        for i in inf:
            for _ in range(K):
                print(i, end=' ')
        print()