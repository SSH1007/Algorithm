r,c = map(int,input().split())
b = []
for _ in range(r):
    a = input()
    b.append(a[::-1])
for n in b:
    print(n)