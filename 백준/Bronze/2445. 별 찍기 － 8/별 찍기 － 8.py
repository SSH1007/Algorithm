N= int(input())
arr = []
for i in range(1,N+1):
    print('*'*i, ' '*2*(N-i), '*'*i, sep='')
for i in range(N-1,0,-1):
    print('*'*i, ' '*2*(N-i), '*'*i, sep='')