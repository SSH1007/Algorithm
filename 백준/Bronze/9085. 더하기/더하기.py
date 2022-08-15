lst = []
T = int(input())
for _ in range(T):
    _ = input()
    lst.append(list(map(int,input().split())))
for l in lst:
    print(sum(l))