T = int(input())
for _ in range(T):
    S = list(set(list(input())))
    hap = 2015
    for s in S:
        hap-=ord(s)
    print(hap)