A, B = map(int, input().split())
a, b = 1, A-1
for _ in range(B):
    a += b
    b += (A-2)
print(a)