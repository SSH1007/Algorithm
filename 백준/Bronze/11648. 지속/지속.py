import sys
input = sys.stdin.readline
n = int(input().rstrip())
dap = 0
while 1:
    if len(str(n)) == 1:
        break
    tmp = 1
    for i in str(n):
        tmp *= int(i)
    n = tmp
    dap += 1
print(dap)