def calc(a, b, cal):
    if cal == '+':
        return a+b
    elif cal == '-':
        return a-b
    elif cal == '*':
        return a*b
    else:
        if a < 0 or b < 0:
            return (abs(a)//abs(b))*-1
        else:
            return a//b


K1, O1, K2, O2, K3 = input().split()
a = calc(calc(int(K1), int(K2), O1), int(K3), O2)
b = calc(int(K1), calc(int(K2), int(K3), O2), O1)
print(min(a, b))
print(max(a, b))