def solution(my_string):
    answer = [0]*52
    for m in my_string:
        o = ord(m)
        if o >= 97:
            answer[o-97+26] += 1
        else:
            answer[o-65] += 1
    return answer