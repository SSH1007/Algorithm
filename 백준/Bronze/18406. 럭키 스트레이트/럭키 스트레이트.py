N = input()
A = N[:len(N)//2]
B = N[len(N)//2:]
aCnt, bCnt = 0, 0
for a in A:
    aCnt+=int(a)
for b in B:
    bCnt+=int(b)
if aCnt==bCnt:
    print('LUCKY')
else:
    print('READY')