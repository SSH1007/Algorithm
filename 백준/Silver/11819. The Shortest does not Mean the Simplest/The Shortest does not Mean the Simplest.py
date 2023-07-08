def fpow(A, B, C):
    dap = 1
    while B:
        if B & 1:
            dap *= A
            dap %= C
        A *= A
        A %= C
        B //= 2
    return dap


A, B, C = map(int, input().split())
print(fpow(A, B, C))