N = input()
dap = 0
startN= int(N)
while 1:
    if startN<0:
        break
    bigyo=0
    for s in str(startN):
        bigyo+=int(s)
    if int(N)==bigyo+startN:
        dap=startN
    startN-=1
print(dap)