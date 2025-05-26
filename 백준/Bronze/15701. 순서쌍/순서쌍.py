def F(n):
    dap = 1
    i = 2
    while i * i <= n:
        tmp = 0
        while n % i == 0:
            n //= i
            tmp += 1
        dap *= (tmp + 1)
        i += 1
    if n > 1:
        dap *= 2
    return dap


print(F(int(input())))