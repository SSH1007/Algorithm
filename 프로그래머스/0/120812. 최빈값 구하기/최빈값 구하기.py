def solution(array):
    dic = dict()
    for a in array:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    lst = sorted(list(dic.items()), key=lambda x:x[1])
    for a, b in lst[:-1]:
        if lst[-1][1] == b:
            return -1
    answer = lst[-1][0]
    return answer