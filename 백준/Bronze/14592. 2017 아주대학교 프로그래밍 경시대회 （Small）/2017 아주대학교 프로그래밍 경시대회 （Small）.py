N = int(input())
lst = []
for n in range(N):
    S, C, L = map(int, input().split())
    lst.append((S, C, L, n+1))
lst.sort(key=lambda x:(-x[0], x[1], x[2]))
print(lst[0][3])