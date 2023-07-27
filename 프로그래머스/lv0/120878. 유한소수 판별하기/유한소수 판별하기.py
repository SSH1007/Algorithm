def GCD(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def solution(a, b):
    answer = 1
    gcd = GCD(a, b)
    a//=gcd
    b//=gcd
    while b!=1:
        if b % 2 == 0:
            b//=2
        elif b % 5 == 0:
            b//=5
        else:
            answer = 2
            break
    return answer