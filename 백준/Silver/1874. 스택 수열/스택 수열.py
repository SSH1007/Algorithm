cnt = 1
stack = []
dap = []
possible = True
N = int(input())
for _ in range(N):
    num = int(input())
    while cnt<=num:
        stack.append(cnt)
        dap.append('+')
        cnt+=1
    if stack[-1] == num:
        stack.pop()
        dap.append('-')
    else:
        possible = False
        break
if possible:
    for d in dap:
        print(d)
else:
    print('NO')