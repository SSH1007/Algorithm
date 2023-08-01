def solution(n):
    answer = -1
    x = (n**0.5)
    if x%1 == 0:
        answer = (x+1)**2
        
    return answer