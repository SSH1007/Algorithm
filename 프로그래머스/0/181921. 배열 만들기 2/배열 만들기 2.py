def solution(l, r):
    answer = []
    for i in range(l, r+1):
        tmp = str(i)
        if set(tmp) == {'0', '5'} or set(tmp) == {'5'}:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer