T = int(input())
for _ in range(T):
    M, type = input().split()
    dap = []
    if type == 'C':
        lst = list(input().split())
        for l in lst:
            dap.append(ord(l)-64)
    else:
        lst = list(map(int, input().split()))
        for l in lst:
            dap.append(chr(l+64))
    print(*dap)