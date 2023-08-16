def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    idx = 0
    while idx < len(score):
        tmp = score[idx:idx+m]
        if len(tmp) == m:
            answer += min(tmp)*m
        idx += m
    
    return answer