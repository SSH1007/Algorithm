S = list(input())
stack = []
for i in range(len(S)):
    if S[i].isdigit():
        stack.append(S[i])
    else:
        s2 = stack.pop()
        s1 = stack.pop()
        if S[i] == '+':
            stack.append(str(int(s1)+int(s2)))
        elif S[i] == '*':
            stack.append(str(int(s1)*int(s2)))
        elif S[i] == '-':
            stack.append(str(int(s1)-int(s2)))
        elif S[i] == '/':
            stack.append(str(int(s1)//int(s2)))
print(*stack)