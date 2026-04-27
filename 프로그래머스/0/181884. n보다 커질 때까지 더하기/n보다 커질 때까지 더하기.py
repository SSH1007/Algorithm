def solution(numbers, n):
    answer = 0
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer