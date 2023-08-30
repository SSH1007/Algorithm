def solution(participant, completion):
    answer = ''
    dic = dict()
    for p in participant:
        if not p in dic:
            dic[p] = 1
        else:
            dic[p] += 1
    for c in completion:
        if c in dic:
            dic[c] -= 1
    a = sorted(list(dic.items()), key=lambda x:-x[1])
    answer = a[0][0]
    return answer