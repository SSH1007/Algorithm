def solution(strArr):
    answer = 0
    dic = dict()
    for s in strArr:
        if not len(s) in dic:
            dic[len(s)] = 1
        else:
            dic[len(s)] += 1
    answer = max(dic.values())
    return answer