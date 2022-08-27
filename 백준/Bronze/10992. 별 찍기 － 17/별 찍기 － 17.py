N = int(input())
for n in range(1,N+1):
    print((N-n)*' ', end='')
    if N >= 3 and n!=1 and n!=N:
        print('*' + (2*(n-1)-1)*' ' + '*')
    else:
        print('*'*(2*n-1))