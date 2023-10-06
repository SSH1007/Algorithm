N = int(input())
for n in range(1, N+1):
    m = int(input())
    lst = []
    for _ in range(m):
        lst.append(int(input())+1)
    print('Case %d:' % n)
    for l in lst:
        if l<=6:
            print(l)