N, L = map(int, input().split())
lst = []
for _ in range(N):
    l = list(input().split('0'))
    lst.append(len(l)-l.count(''))
m = max(lst)
print(m, lst.count(m))