N = int(input())
s = set()
for i in range(1, N+1):
    if N%i == 0:
        s.add(i)
print(sum(list(s)))