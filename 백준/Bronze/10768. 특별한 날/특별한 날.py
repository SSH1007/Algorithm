M = int(input())
D = int(input())
def sp(m,d):
    if m == 2:
        if d<18:
            return 'Before'
        elif d==18:
            return 'Special'
        else:
            return 'After'
    elif m < 2:
        return 'Before'
    elif m > 2: 
        return 'After'
print(sp(M,D))
