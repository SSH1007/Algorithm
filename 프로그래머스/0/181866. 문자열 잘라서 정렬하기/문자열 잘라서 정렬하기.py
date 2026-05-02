def solution(myString):
    tmp = sorted(list(myString.split('x')))
    answer = []
    for t in tmp:
        if t != '':
            answer.append(t)
    return answer