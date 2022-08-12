import sys
input=sys.stdin.readline
N=int(input())
for n in range(1,N+1):
    print((N-n)*' ', (2*n-1)*'*', sep ='')
for n in range(N-1,0,-1):
    print((N-n)*' ', (2*n-1)*'*', sep ='')