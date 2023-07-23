def solution(myString, pat):
    answer = 0
    tmp = ''
    for m in myString:
        if m == 'A':
            tmp+='B'
        else:
            tmp+='A'
    if pat in tmp:
        answer = 1
    return answer