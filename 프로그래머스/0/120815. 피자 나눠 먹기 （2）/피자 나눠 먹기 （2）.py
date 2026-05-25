def GCD(a, b):
    while b:
        a, b = b, a%b
    return a

def solution(n):
    gcd = GCD(n, 6)
    lcm = (n*6)//gcd
    answer = lcm//6
    return answer