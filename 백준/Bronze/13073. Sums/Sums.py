t = int(input())
for _ in range(t):
    N = int(input())
    S1 = N*(N+1)//2
    S2 = 2*N*N//2
    S3 = (2+2*N)*N//2
    print(S1, S2, S3)