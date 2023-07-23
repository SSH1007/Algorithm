def cross(A, B):
    N = len(A)
    M = len(B)
    for a in range(N):
        for b in range(M):
            if A[a] == B[b]:
                return a,b

A, B = input().split()
a, b = cross(A, B)
graph = [['']*(len(A)) for _ in range(len(B))]

for m in range(len(B)):
    for n in range(len(A)):
        if n == a:
            graph[m][n] = B[m]
        elif m == b:
            graph[m][n] = A[n]
        else:
            graph[m][n] = '.'
for g in graph:
    print(*g, sep='')