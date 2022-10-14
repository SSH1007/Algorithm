while 1:
    stack = []
    string = input()
    if string == '.':
        break
    for s in string:
        if s == '(':
            stack.append('(')
        elif s == '[':
            stack.append('[')
        elif s == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
        elif s == ']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(']')
    else:
        stack.append('yeah')
    stack.pop()
    print('yes' if not len(stack) else 'no')