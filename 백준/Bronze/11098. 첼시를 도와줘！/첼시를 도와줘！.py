N = int(input())
for n in range(N):
    lst = []
    P = int(input())
    for p in range(P):
        price, name = input().split()
        lst.append((int(price),name))
    lst.sort()
    print(lst[-1][1])