def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer = numer1*denom2+numer2*denom1
    denom = denom1*denom2
    
    answer.append(numer//GCD(numer, denom))
    answer.append(denom//GCD(numer, denom))
    
    return answer