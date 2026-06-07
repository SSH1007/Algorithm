def solution(age):
    answer = ''
    while age > 0:
        a = age%10
        answer = chr(a+97) + answer
        age //= 10
    return answer