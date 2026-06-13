def F(n):
    d = 1
    for i in range(1, n+1):
        d *= i
    return d

def solution(balls, share):
    answer = F(balls)//(F(balls-share)*F(share))
    return answer