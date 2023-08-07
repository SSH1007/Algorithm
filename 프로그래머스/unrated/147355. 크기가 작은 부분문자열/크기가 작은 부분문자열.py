def solution(t, p):
    answer = 0
    l = len(p)
    n = len(t)
    for i in range(n-l+1):
        if int(t[i:i+l]) <= int(p):
            answer += 1
        
    return answer