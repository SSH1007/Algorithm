N = int(input())
X = int(input())
lst = []
while 1:
    try:
        maps = list(map(int, input().split()))
        lst.append(maps)
    except EOFError:
        break
dap = 0
n = len(lst)-1
while n > -1:
    if len(lst[n]) == 1:
        dap += lst[n][0]
        n -= 2
    else:
        dap += max(lst[n])
        n -= 1
print(dap)