def fpow(A, B, C):
    if B == 1:
        return A%C
    else:
        x = fpow(A, B//2, C)
        if B % 2 == 0:
            return (x * x)%C
        else:
            return (x * x * A)%C

A, B, C = map(int, input().split())
print(fpow(A,B,C))