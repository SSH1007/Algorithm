def fact(m):
    if m==0:
        return 1
    return fact(m-1)*m

N,K = map(int,input().split())
print(fact(N)//(fact(K)*fact(N-K)))