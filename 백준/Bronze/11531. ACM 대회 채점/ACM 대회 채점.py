lst = [[0]*26 for _ in range(2)]
while 1:
    ipt = input().split()
    if ipt[0] == '-1':
        break
    m, nme, res = int(ipt[0]), ipt[1], ipt[2]
    if res == 'right':
        lst[1][ord(ipt[1])-65] = 1
        lst[0][ord(ipt[1])-65] += m
    else:
        lst[0][ord(ipt[1])-65] += 20
dap = 0
for i in range(26):
    if lst[1][i] == 1:
        dap += lst[0][i]
print(sum(lst[1]), dap)