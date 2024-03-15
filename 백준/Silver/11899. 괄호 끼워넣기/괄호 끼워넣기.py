from collections import deque
que = deque(input())
stack = []
while que:
    a = que.popleft()
    if a == '(':
        stack.append(a)
    elif stack and stack[-1] == '(' and a == ')':
        stack.pop()
    else:
        stack.append(a)
print(len(stack))