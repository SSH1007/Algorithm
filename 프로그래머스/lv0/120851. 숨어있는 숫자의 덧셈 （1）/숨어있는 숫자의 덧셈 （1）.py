def solution(my_string):
    answer = 0
    for m in my_string:
        if m.isdigit():
            answer += int(m)
    return answer