N = int(input())
S = input()
numbers = []
for _ in range(N):
    n = int(input())
    numbers.append(n)

stack = []
for s in S:
    if s in ['+', '-', '*', '/']:
        b = stack.pop()
        a = stack.pop()
        if s == '+':
            stack.append(a+b)
        elif s == '-':
            stack.append(a-b)
        elif s == '*':
            stack.append(a*b)
        elif s == '/':
            stack.append(a/b)
    else:
        stack.append(numbers[ord(s)-65])
print(f'{stack[0]:.2f}')