T = int(input())
for _ in range(T):
    a,b,c,d,e = input().split()
    flag = False
    if b == '+':
        if int(a)+int(c) == int(e):
            flag = True
    elif b == '-':
        if int(a)-int(c) == int(e):
            flag = True
    elif b == '*':
        if int(a)*int(c) == int(e):
            flag = True
    elif b == '/':
        if int(a)//int(c) == int(e):
            flag = True
    if flag:
        print('correct')
    else:
        print('wrong answer')