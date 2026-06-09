def solution(emergency):
    answer = []
    newE = sorted(emergency, key=lambda x:-x)
    dic = dict()
    for i, n in enumerate(newE):
        dic[n] = i+1
    for e in emergency:
        answer.append(dic[e])
    return answer