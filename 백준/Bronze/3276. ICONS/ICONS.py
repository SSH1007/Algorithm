N = int(input())
m = 101
a, b = 0, 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if N <= i*j and i+j < m:
            m = i+j
            a, b = i, j
print(a, b)