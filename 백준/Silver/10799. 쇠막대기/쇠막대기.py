S = input()
stack = []
dap = 0
for i in range(len(S)):
    if S[i] == '(':
        stack.append('(')
    elif S[i] == ')':
        if S[i-1] != '(':
            stack.pop()
            dap += 1
        elif stack[-1] == '(':
            stack.pop()
            dap += len(stack)
print(dap)