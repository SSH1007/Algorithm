N = int(input())
for n in range(1,N+1):
    print(n, end=' ')
    if n%6==0:
        print('Go!', end=' ')
    elif n==N:
        print('Go!', end=' ')