def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        tmp = ''
        if i%2: 
            for s in strArr[i]:
                tmp += s.upper()
            answer.append(tmp)
        else:
            for s in strArr[i]:
                tmp += s.lower()
            answer.append(tmp)
    return answer