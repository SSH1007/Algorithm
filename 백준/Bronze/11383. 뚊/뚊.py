N, M = map(int, input().split())
l = []
ll = []
for _ in range(N):
    A = input()
    l.append(A)
for _ in range(N):
    B = input()
    ll.append(B)
for i in range(N):
    C = ''
    for j in l[i]:
        C += j*2
    if C != ll[i]:
        print('Not Eyfa')
        break
else:
    print('Eyfa')