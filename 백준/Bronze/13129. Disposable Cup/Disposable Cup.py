A, B, N = map(int, input().split())
lst = []
for n in range(1, N+1):
    lst.append(A*N+B*n)
print(*lst)