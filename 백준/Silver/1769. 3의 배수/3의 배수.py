X = input()
cnt, dap = 0, int(X)
while len(X)>1:
    dap = 0
    for x in X:
        dap += int(x)
    X = str(dap)
    cnt+=1
print(cnt)
print('YES' if dap%3==0 else 'NO')