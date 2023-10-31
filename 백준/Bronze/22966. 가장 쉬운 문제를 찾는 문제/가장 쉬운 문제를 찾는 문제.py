N = int(input())
lst = []
for _ in range(N):
    a, b = input().split()
    b = int(b)
    lst.append((a, b))
lst.sort(key=lambda x: x[1])
print(lst[0][0])