def solution(n):
    answer = 0
    a = n//7
    b = n%7
    if b:
        answer = a+1
    else:
        answer = a
    return answer