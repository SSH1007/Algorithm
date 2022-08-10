T = int(input())
for _ in range(T):
    N = int(input())
    Cs, Gs = 0, 0
    for _ in range(N):
        C, G = map(float,input().split())
        Cs+=C
        Gs+=G*C
    print(int(Cs), round(Gs/int(Cs),1))