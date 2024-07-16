import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    stack = []
    dap = 0
    tmp = 1
    bracket = input()
    # 분배법칙
    # 2*(2+3*3) = 2*2 + 2*3*3
    for i in range(len(bracket)):
        if bracket[i] == '(':
            stack.append('(')
            tmp *= 2

        elif bracket[i] == ')':
            # 올바르지 않은 괄호열
            if not stack or stack[-1] == '[':
                dap = 0
                break
            stack.pop()
            if bracket[i-1] == '(':
                dap += tmp
            tmp //= 2

        elif bracket[i] == '[':
            stack.append('[')
            tmp *= 3

        elif bracket[i] == ']':
            # 올바르지 않은 괄호열
            if not stack or stack[-1] == '(':
                dap = 0
                break
            stack.pop()
            if bracket[i-1] == '[':
                dap += tmp
            tmp //= 3

    # 위의 과정을 끝냈는데도 스택에 괄호가 남아있으면 올바르지 않은 괄호열
    if stack:
        dap = 0
    print(dap)


if __name__ == '__main__':
    main()