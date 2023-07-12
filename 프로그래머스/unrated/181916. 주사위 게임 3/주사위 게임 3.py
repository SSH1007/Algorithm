def solution(a, b, c, d):
    answer = 0
    dic = dict()
    lst = [a,b,c,d]
    for l in lst:
        if l not in dic:
            dic[l] = 1
        else:
            dic[l] += 1
    newlst = list(dic.items())
    newlst.sort(key= lambda x : x[1])
    print(newlst)
    if len(newlst) == 1:
        answer = newlst[0][0]*1111
    elif len(newlst) == 2 and newlst[1][1] == 3:
        answer = (newlst[1][0]*10 + newlst[0][0])**2
    elif len(newlst) == 2:
        answer = (newlst[0][0]+newlst[1][0])*abs(newlst[0][0]-newlst[1][0])
    elif len(newlst) == 3:
        answer = newlst[0][0]*newlst[1][0]
    else:
        newlst.sort(key = lambda x : x[0])
        answer = newlst[0][0]
    return answer