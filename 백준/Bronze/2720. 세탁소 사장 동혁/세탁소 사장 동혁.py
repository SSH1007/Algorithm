T = int(input())
for _ in range(T):
    C = int(input())
    Q = C//25
    C-=(Q*25)
    D = C//10
    C-=(D*10)
    N = C//5
    C-=(N*5)
    P = C
    print(Q,D,N,P)