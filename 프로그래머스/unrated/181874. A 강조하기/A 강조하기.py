def solution(myString):
    answer = ''
    for m in myString:
        if m == 'a':
            answer += m.upper()
        elif m == 'A':
            answer += 'A'
        else:
            answer += m.lower()
    return answer