def solution(spell, dic):
    answer = 0
    for d in dic:
        flag = False
        dap = 0
        for s in spell:
            if d.count(s) == 1:
                dap += 1
        if dap == len(spell):
            flag = True
            break
    if flag:
        answer = 1
    else:
        answer = 2
    return answer