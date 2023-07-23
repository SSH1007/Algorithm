def solution(n):
    answer = 0
    if (n**0.5)%1:
        answer = 2
    else:
        answer = 1
    return answer