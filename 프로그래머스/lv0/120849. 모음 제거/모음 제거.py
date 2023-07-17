def solution(my_string):
    answer = ''
    for m in my_string:
        if m not in ['a','e','i','o','u']:
            answer += m
    return answer