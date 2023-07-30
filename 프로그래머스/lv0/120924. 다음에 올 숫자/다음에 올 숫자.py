def solution(common):
    answer = 0
    if common[0] == 0 or common[1] == 0:
        answer = common[-1] + (common[1]-common[0])
    else:
        if common[2]/common[1] == common[1]/common[0]:
            answer = common[-1]*(common[1]/common[0])
        else:
            answer = common[-1]+(common[1]-common[0])
    return answer