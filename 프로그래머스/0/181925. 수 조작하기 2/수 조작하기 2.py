def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        a = numLog[i]
        b = numLog[i-1]
        if a == b+1:
            answer += 'w'
        elif a == b-1:
            answer += 's'
        elif a == b+10:
            answer += 'd'
        else:
            answer += 'a'
    return answer