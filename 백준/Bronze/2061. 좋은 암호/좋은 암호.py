K, L = map(int, input().split())
sosu = [1]*(L+1)
sosu[0], sosu[1] = 0, 0
a = int(L**0.5)+1 
for i in range(2,a):
    if sosu[i]:
        for j in range(i*i, L+1, i):
            sosu[j] = 0
for i in range(2, L+1):
    if sosu[i]:
        if K%i==0:
            if i<L:
                print('BAD',i)
                break
else:
    print('GOOD')