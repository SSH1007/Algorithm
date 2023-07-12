# 15  1 2 3 4 5 6 7 8 9
# 6   10 11 12 13 14 15
# 15개의 1의 자리수, 6개의 2의 자리수
N = int(input())
dap = 0
if N < 10:
    print(N)
else:
    i = 1
    while i <= N:
        dap += N-i+1
        i *= 10
    print(dap)