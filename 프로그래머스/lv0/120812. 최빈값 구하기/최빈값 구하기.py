def solution(array):
    answer = 0
    dic = dict()
    for a in array:
        if a not in dic:
            dic[a] = 1
        else:
            dic[a] += 1
    lst = list(dic.items())
    lst.sort(key = lambda x : x[1], reverse = True)
    if len(lst)>1 and lst[0][1] == lst[1][1]:
        answer = -1
    else:
        answer = lst[0][0]
        
    return answer