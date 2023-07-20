def solution(s):
    answer = ''
    dic = dict()
    for ss in s:
        if ss not in dic:
            dic[ss] = 1
        else:
            dic[ss] += 1
    lst = [i for i in list(dic.items()) if i[1] == 1]
    lst.sort()
    for l in lst:
        answer += l[0]
    return answer