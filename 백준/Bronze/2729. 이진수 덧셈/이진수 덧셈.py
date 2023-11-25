T = int(input())
for _ in range(T):
    A, B = input().split()
    dap = bin(int(A, 2)+int(B, 2))
    print(dap[2:])