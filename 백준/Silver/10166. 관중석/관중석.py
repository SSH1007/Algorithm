s = set()
D1, D2 = map(int, input().split())
for i in range(D1, D2+1):
    for j in range(1, i+1):
        s.add(j/i)
print(len(s))