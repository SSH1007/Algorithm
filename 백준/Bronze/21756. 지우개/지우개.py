N = int(input())
A = [n for n in range(1, N+1)]

while N>1:
    B = [A[n] for n in range(N) if n%2]
    N = len(B)
    A = B[:]
print(*A)