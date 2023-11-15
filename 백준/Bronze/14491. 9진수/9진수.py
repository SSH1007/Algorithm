T = int(input())
dap = []
while T:
    dap.append(T % 9)
    T //= 9
print(''.join(map(str, dap[::-1])))