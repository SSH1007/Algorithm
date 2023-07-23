def solution(myString):
    answer = []
    tmp = ''
    for m in range(len(myString)):
        if myString[m] != 'x':
            tmp+=myString[m]
        else:
            if tmp != '':
                answer.append(tmp)
            tmp = ''
    if tmp != '':
        answer.append(tmp)
    answer.sort()
    return answer