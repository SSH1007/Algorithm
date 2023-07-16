def solution(my_string):
    answer = [0]*(52)
    for m in my_string:
        if ord(m) < 97:
            answer[ord(m)-65] += 1
        else:
            answer[ord(m)-71] += 1
    return answer