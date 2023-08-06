def GCD(a, b):
    while b != 0:
        a, b = b, a%b
    return a
    

def solution(n, m):
    gcd = GCD(n, m)
    answer = [gcd, (n*m)//gcd]
    return answer