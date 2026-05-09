def solution(myString):
    answer = ''
    for m in myString:
        if ord(m) < ord('l'):
            answer += 'l'
        else:
            answer += m
    return answer