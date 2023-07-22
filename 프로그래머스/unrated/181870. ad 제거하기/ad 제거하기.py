def solution(strArr):
    answer = []
    for strA in strArr:
        if 'ad' not in strA:
            answer.append(strA)
    return answer