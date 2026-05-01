def solution(strArr):
    answer = []
    for s in strArr:
        if not 'ad' in s:
            answer.append(s)
    return answer