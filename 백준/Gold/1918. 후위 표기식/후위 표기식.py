N = input()
stack = []
dap = ''
for n in N:
    if n.isalpha():
        dap += n
    else:
        # 괄호라면?
        if n == '(':
            stack.append(n)
        elif n == ')':
            while stack and stack[-1] != '(':
                dap += stack.pop()
            stack.pop()
        # 곱셈/나눗셈이라면?
        elif n == '*' or n == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                dap += stack.pop()
            stack.append(n)
        # 덧셈/뺄셈이라면?
        else:
            while stack and stack[-1] != '(':
                dap += stack.pop()
            stack.append(n)
# 스택에 남은거 처리
while stack:
    dap += stack.pop()
print(dap)