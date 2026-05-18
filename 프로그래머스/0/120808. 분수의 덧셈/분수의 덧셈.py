def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom3 = denom1*denom2
    numer3 = numer1*denom2+numer2*denom1
    gcd = GCD(denom3, numer3)
    answer.append(numer3//gcd)
    answer.append(denom3//gcd)
    return answer