M = int(input())
N = int(input())
sn = 0
a = []
for i in range(M, N+1):
    if ((i**0.5)*10) % 10 == 0:
        a.append(i)
        sn += i
if sn:
    print(sn, min(a), sep='\n')
else:
    print(-1)