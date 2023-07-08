def solution(slice, n):
    answer = 0
    while 1:
        if answer * slice >= n:
            break
        answer += 1
    return answer