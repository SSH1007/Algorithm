def solution(X, Y):
    answer = ''
    for t in range(9, -1, -1):
        answer += str(t)*min(X.count(str(t)), Y.count(str(t)))
    if len(answer) < 1:
        answer = '-1'
    elif len(answer) == answer.count('0'):
        answer = '0' 
        
    return answer