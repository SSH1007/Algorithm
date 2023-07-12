def solution(x, n):
    answer = []
    y = x
    while n > 0:
        answer.append(y)
        y+=x
        n-=1
        
    return answer