def solution(myStr):
    answer = []
    
    tmp = ''
    for i in range(len(myStr)):
        if myStr[i] not in ['a', 'b', 'c']:
           tmp += myStr[i]
        else:
            if tmp != '':
                answer.append(tmp)
            tmp = ''
    if tmp != '':
        answer.append(tmp)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer