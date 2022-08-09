M,N=map(int,input().split())
lst=[True]*(N+1)
lst[1]=False
for i in range(2,int(N**0.5)+1):
    if lst[i]:
        for j in range(i*i,N+1,i):
            lst[j]=False
for i in range(M,N+1):
    if lst[i]:
        print(i)