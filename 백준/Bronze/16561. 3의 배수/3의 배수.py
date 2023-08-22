n = int(input())
N = n//3
lst = [0]*(N+1)
s = 0
for i in range(1, N+1):
    lst[i] = lst[i-1] + s
    s+= 1
print(lst[N-1])