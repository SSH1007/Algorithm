def multiply(X):
    dap = 1
    for x in X:
       dap*=int(x)
    return dap

N = input()
if len(N)==1:
    print('NO')
else:
    flag = False
    for i in range(1,len(N)):
        front = N[:i]
        rear = N[i:]
        if multiply(front) == multiply(rear):
            flag = True
    if flag:
        print('YES')
    else:
        print('NO')