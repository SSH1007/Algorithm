def hanoi(token, start, by, to):
    if token == 1:
        print(start, to)
        return
    hanoi(token-1, start, to, by)
    print(start, to)
    hanoi(token-1, by, start, to)


N = int(input())
dap = 2**N-1
print(dap)
if N <= 20:
    hanoi(N, 1, 2, 3)