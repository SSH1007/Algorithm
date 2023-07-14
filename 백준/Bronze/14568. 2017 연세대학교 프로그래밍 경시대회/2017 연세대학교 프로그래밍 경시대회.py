N = int(input())
lst = []
for t in range(2, N, 2):
    for y in range(1, N):
        for n in range(y+2, N):
            if y+t+n == N:
                lst.append((t,y,n))
print(len(lst))