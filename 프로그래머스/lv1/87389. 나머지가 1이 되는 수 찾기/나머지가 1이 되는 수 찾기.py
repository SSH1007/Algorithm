def solution(n):
    answer = 0
    for x in range(2,n):
        if n%x == 1:
            answer = x
            break
    return answer