def solution(name, yearning, photo):
    answer = []
    dic = dict()
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for ph in photo:
        dap = 0 
        for p in ph:
            if p in dic:
                dap += dic[p]
        answer.append(dap)
    return answer