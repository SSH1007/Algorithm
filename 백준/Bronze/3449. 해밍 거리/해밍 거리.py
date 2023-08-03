T = int(input())
for _ in range(T):
    a = input()
    b = input()
    dap = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dap+=1
    print(f'Hamming distance is {dap}.')