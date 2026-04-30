def solution(myString):
    answer = ''
    for m in myString:
        if m.lower() == 'a':
            answer += 'A'
        else:
            answer += m.lower()
    return answer