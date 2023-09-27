N, M = map(int, input().split())
friend = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    friend[A-1].append(B)
    friend[B-1].append(A)
for f in friend:
    print(len(f))