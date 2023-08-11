def solution(a, b, n):
    answer = 0
    while n >= a:
        tmp = n//a
        n-=tmp*a
        n+=tmp*b
        answer += tmp*b
        
    return answer