N = int(input())
lst = []
for _ in range(N):
    lst.append(input())
for i in range(1, 101):
    s = set()
    for j in range(N):
        num = '000'+lst[j]
        s.add(num[-i:])
    if len(s) == N:
        print(i)
        break