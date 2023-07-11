def solution(l, r):
    answer = []
    for i in range(l, r+1):
        S = sorted(list(set(str(i)))) 
        if S == ['0','5'] or S ==['0'] or S ==['5']:
            answer.append(i)
    else:
        answer.append(-1)
    if len(answer)>1:
        answer.pop()
    return sorted(answer)