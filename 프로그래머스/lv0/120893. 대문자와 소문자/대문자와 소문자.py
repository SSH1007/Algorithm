def solution(my_string):
    answer = ''
    for m in my_string:
        if ord(m) > 91:
            answer += chr(ord(m)-32)
        else:
            answer += chr(ord(m)+32)
    return answer 