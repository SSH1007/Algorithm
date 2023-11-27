def solution(keymap, targets):
    answer = []
    dic = dict()    
    
    for key in keymap:
        for idx, k in enumerate(key):
            if k in dic and idx > dic[k]:
                continue
            dic[k] = idx
            
    
    for tar in targets:
        tmp = 0
        for t in tar:
            if t not in dic:
                tmp = -1
                break
            else:
                tmp += (dic[t]+1)
        answer.append(tmp)
    return answer