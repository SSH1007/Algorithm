def viva(a,b,c,d):
    global dap
    if abs(a-b) == abs(b-c) == abs(c-d) == abs(d-a):
        if dap>0:
            dap+=1
        return
    dap+=1
    viva(abs(a-b),abs(b-c),abs(c-d),abs(d-a))

while 1:
    dap = 0
    a,b,c,d = map(int, input().split())
    if a==b==c==d==0:
        break
    viva(a,b,c,d)
    print(dap)