N = int(input())
for n in range(2, N):
    if N % n != 0:
        print(n, end=' ')
        break
for n in range(N-1, 1, -1):
    if N % n != 0:
        print(n)
        break