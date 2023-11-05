T = int(input())
for _ in range(T):
    S = input()
    SS = S+S
    A, B = [], []
    for i in range(len(SS)):
        if i%2:
            B.append(SS[i])
        else:
            A.append(SS[i])
    As = ''.join(A)
    Bs = ''.join(B)
    if len(As)%2 == 0:
        As = As[:len(As)//2]
    if len(Bs)%2 == 0:
        Bs = Bs[:len(Bs)//2]
    print(As)
    print(Bs)