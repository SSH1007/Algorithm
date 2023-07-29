def solution(myString):
    answer = ''
    for m in myString:
        if ord(m) < 108:
            answer += 'l'
        else:
            answer += m
            
    return answer