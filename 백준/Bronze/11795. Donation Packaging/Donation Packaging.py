T = int(input())
As, Bs, Cs = 0, 0, 0
for _ in range(T):
    A, B, C = map(int, input().split())
    As += A
    Bs += B
    Cs += C
    if As >= 30 and Bs >= 30 and Cs >= 30:
        M = min((As, Bs, Cs))
        print(M)
        As -= M
        Bs -= M
        Cs -= M
    else:
        print('NO')