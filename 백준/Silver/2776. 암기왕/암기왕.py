T = int(input())
for _ in range(T):
    N = int(input())
    Nlst = list(map(int, input().split()))
    Ndic = dict()
    for l in Nlst:
        Ndic[l] = 1
    M = int(input())
    Mlst = list(map(int, input().split()))
    for l in Mlst:
        try:
            print(Ndic[l])
        except:
            print(0)