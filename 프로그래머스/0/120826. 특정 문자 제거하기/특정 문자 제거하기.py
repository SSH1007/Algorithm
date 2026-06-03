def solution(my_string, letter):
    answer = ''
    for m in my_string:
        if m == letter:
            continue
        answer += m
    return answer