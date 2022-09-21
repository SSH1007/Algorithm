T = int(input())
for _ in range(T):
    S = input()
    stack = []
    for s in S:
        if s=='(':
            stack.append(1)
        else:
            try:
                stack.pop()
            except:
                print('NO')
                break
    else:
        print('YES' if len(stack)<1 else 'NO')