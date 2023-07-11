def solution(my_string, letter):
    answer = ''
    for m in my_string:
        if m != letter:
            answer+=m
    return answer