N, K = map(int, input().split())
lst = list(map(int, input().split(',')))
A = lst
B = []
for _ in range(K):
    for a in range(len(A)-1):
        B.append(A[a+1]-A[a])
    A, B = B, []
print(*A, sep=',')