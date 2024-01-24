# 3진수
# 1 1
# 3 10
# 4 11
# 9 100
# 10 101
# 12 110
# 13 111
# 27 1000
# 28 1001
# 30 1010

N = bin(int(input()))[2:]
dap = 0
for i in range(len(N)):
    if N[i] == '1':
        dap += 3**(len(N)-i-1)
print(dap)